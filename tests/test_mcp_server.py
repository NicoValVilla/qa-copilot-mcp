from src.infrastructure.mcp import MCPClient, build_mcp_server


def test_mcp_client_discovers_registered_tools() -> None:
    client = MCPClient(build_mcp_server())

    tool_names = {tool["name"] for tool in client.discover_tools()}

    assert "generar_casos_prueba" in tool_names
    assert "generar_criterios_aceptacion" in tool_names
    assert "analizar_riesgos" in tool_names
    assert "estimar_esfuerzo_qa" in tool_names


def test_testing_tool_generates_security_cases() -> None:
    client = MCPClient(build_mcp_server())

    result = client.execute_tool(
        "generar_casos_prueba",
        {
            "titulo": "Agregar autenticación con Google",
            "descripcion": "Los usuarios deben poder iniciar sesión usando OAuth2 con Google.",
            "tipo": "Story",
        },
    )

    assert "casos_positivos" in result
    assert any("Google" in item for item in result["casos_positivos"])
