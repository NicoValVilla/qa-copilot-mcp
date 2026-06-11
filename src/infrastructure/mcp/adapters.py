from src.domain.entities import JiraTicket
from src.domain.ports import (
    AcceptanceCriteriaPort,
    EffortEstimationPort,
    RiskAnalysisPort,
    TestingAnalysisPort,
)
from src.infrastructure.mcp.client import MCPClient


class MCPTestingAnalysisAdapter(TestingAnalysisPort):
    def __init__(self, client: MCPClient) -> None:
        self._client = client

    def generar_casos_prueba(self, ticket: JiraTicket) -> dict:
        return self._client.execute_tool("generar_casos_prueba", ticket.model_dump())


class MCPAcceptanceCriteriaAdapter(AcceptanceCriteriaPort):
    def __init__(self, client: MCPClient) -> None:
        self._client = client

    def generar_criterios(self, ticket: JiraTicket) -> dict:
        return self._client.execute_tool("generar_criterios_aceptacion", ticket.model_dump())


class MCPRiskAnalysisAdapter(RiskAnalysisPort):
    def __init__(self, client: MCPClient) -> None:
        self._client = client

    def analizar_riesgos(self, ticket: JiraTicket) -> dict:
        return self._client.execute_tool("analizar_riesgos", ticket.model_dump())


class MCPEffortEstimationAdapter(EffortEstimationPort):
    def __init__(self, client: MCPClient) -> None:
        self._client = client

    def estimar_esfuerzo(self, ticket: JiraTicket) -> dict:
        return self._client.execute_tool("estimar_esfuerzo_qa", ticket.model_dump())
