from typing import Protocol

from src.domain.entities import JiraTicket


class TestingAnalysisPort(Protocol):
    def generar_casos_prueba(self, ticket: JiraTicket) -> dict:
        """Genera casos positivos, negativos y borde."""
