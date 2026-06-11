import asyncio
import json
import os
import shlex
import sys
from typing import Any


class StdioMCPClient:
    """MCP client backed by the official Python SDK over stdio."""

    def __init__(
        self,
        command: str,
        args: list[str] | None = None,
        env: dict[str, str] | None = None,
    ) -> None:
        self._command = command
        self._args = args or []
        self._env = env

    @classmethod
    def from_environment(cls) -> "StdioMCPClient":
        command = os.getenv("QA_COPILOT_MCP_COMMAND", sys.executable)
        args = _parse_args(
            os.getenv(
                "QA_COPILOT_MCP_ARGS",
                "-m src.infrastructure.mcp.real_server",
            )
        )
        return cls(command=command, args=args)

    def discover_tools(self) -> list[dict[str, Any]]:
        return asyncio.run(self._discover_tools())

    def execute_tool(self, tool_name: str, payload: dict[str, Any]) -> dict[str, Any]:
        return asyncio.run(self._execute_tool(tool_name, payload))

    async def _discover_tools(self) -> list[dict[str, Any]]:
        session = await self._open_session()
        async with session as mcp_session:
            tools = await mcp_session.list_tools()
            return [
                {
                    "name": tool.name,
                    "description": tool.description or "",
                    "input_schema": getattr(tool, "inputSchema", None)
                    or getattr(tool, "input_schema", {}),
                }
                for tool in tools.tools
            ]

    async def _execute_tool(self, tool_name: str, payload: dict[str, Any]) -> dict[str, Any]:
        session = await self._open_session()
        async with session as mcp_session:
            available_tools = {tool["name"] for tool in await self._discover_tools_in_session(mcp_session)}
            if tool_name not in available_tools:
                raise ValueError(f"La tool '{tool_name}' no fue descubierta por el cliente MCP real.")

            result = await mcp_session.call_tool(tool_name, arguments=payload)
            if result.isError:
                raise RuntimeError(_text_result(result) or f"La tool '{tool_name}' fallo.")

            if result.structuredContent:
                return dict(result.structuredContent)

            text = _text_result(result)
            if text:
                parsed = json.loads(text)
                if isinstance(parsed, dict):
                    return parsed

            return {}

    async def _discover_tools_in_session(self, mcp_session: Any) -> list[dict[str, Any]]:
        tools = await mcp_session.list_tools()
        return [{"name": tool.name} for tool in tools.tools]

    async def _open_session(self) -> Any:
        try:
            from mcp import ClientSession, StdioServerParameters
            from mcp.client.stdio import stdio_client
        except ImportError as exc:
            raise RuntimeError(
                "Falta instalar el SDK oficial de MCP. Ejecuta: pip install -r requirements.txt"
            ) from exc

        server_params = StdioServerParameters(
            command=self._command,
            args=self._args,
            env=self._env,
        )
        transport = stdio_client(server_params)
        read, write = await transport.__aenter__()
        session = ClientSession(read, write)
        await session.__aenter__()
        await session.initialize()
        return _SessionContext(transport, session)


class _SessionContext:
    def __init__(self, transport: Any, session: Any) -> None:
        self._transport = transport
        self._session = session

    async def __aenter__(self) -> Any:
        return self._session

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        await self._session.__aexit__(exc_type, exc, tb)
        await self._transport.__aexit__(exc_type, exc, tb)


def _parse_args(value: str) -> list[str]:
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError:
        return shlex.split(value)

    if not isinstance(parsed, list) or not all(isinstance(item, str) for item in parsed):
        raise ValueError("QA_COPILOT_MCP_ARGS debe ser una cadena shell o un JSON array de strings.")
    return parsed


def _text_result(result: Any) -> str:
    texts: list[str] = []
    for content in result.content:
        text = getattr(content, "text", None)
        if text:
            texts.append(text)
    return "\n".join(texts)
