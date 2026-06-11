import pytest

pytest.importorskip("mcp")

from src.infrastructure.mcp.real_client import StdioMCPClient


def test_stdio_mcp_client_calls_real_server() -> None:
    client = StdioMCPClient.from_environment()

    result = client.execute_tool(
        "estimar_esfuerzo_qa",
        {
            "titulo": "Agregar autenticacion con Google",
            "descripcion": "Los usuarios deben poder iniciar sesion usando OAuth2 con Google.",
            "tipo": "Story",
        },
    )

    assert result["nivel"] == "Alto"
