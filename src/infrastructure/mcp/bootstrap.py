from src.infrastructure.mcp.server import MCPServer
from src.infrastructure.mcp.tools import (
    analizar_riesgos,
    estimar_esfuerzo_qa,
    generar_casos_prueba,
    generar_criterios_aceptacion,
)
from src.infrastructure.mcp.tools.common import JIRA_TICKET_SCHEMA


def build_mcp_server() -> MCPServer:
    server = MCPServer()
    server.register_tool(
        name="generar_casos_prueba",
        description="Genera casos positivos, negativos y borde desde un ticket Jira.",
        input_schema=JIRA_TICKET_SCHEMA,
        handler=generar_casos_prueba,
    )
    server.register_tool(
        name="generar_criterios_aceptacion",
        description="Genera criterios Given / When / Then desde un ticket Jira.",
        input_schema=JIRA_TICKET_SCHEMA,
        handler=generar_criterios_aceptacion,
    )
    server.register_tool(
        name="analizar_riesgos",
        description="Analiza riesgos funcionales, de integración y seguridad.",
        input_schema=JIRA_TICKET_SCHEMA,
        handler=analizar_riesgos,
    )
    server.register_tool(
        name="estimar_esfuerzo_qa",
        description="Estima esfuerzo QA como Bajo, Medio o Alto.",
        input_schema=JIRA_TICKET_SCHEMA,
        handler=estimar_esfuerzo_qa,
    )
    return server
