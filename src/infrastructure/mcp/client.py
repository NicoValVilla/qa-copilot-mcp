from typing import Any

from src.infrastructure.mcp.server import MCPServer


class MCPClient:
    """Cliente MCP educativo que representa el paso Host -> Client -> Server."""

    def __init__(self, server: MCPServer) -> None:
        self._server = server

    def discover_tools(self) -> list[dict[str, Any]]:
        return self._server.list_tools()

    def execute_tool(self, tool_name: str, payload: dict[str, Any]) -> dict[str, Any]:
        available_tools = {tool["name"] for tool in self.discover_tools()}
        if tool_name not in available_tools:
            raise ValueError(f"La tool '{tool_name}' no fue descubierta por el cliente.")
        return self._server.call_tool(tool_name, payload)
