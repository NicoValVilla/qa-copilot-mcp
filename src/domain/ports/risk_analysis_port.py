from typing import Protocol

from src.domain.entities import JiraTicket


class RiskAnalysisPort(Protocol):
    def analizar_riesgos(self, ticket: JiraTicket) -> dict:
        """Analiza riesgos funcionales, de integración y seguridad."""
