from typing import Protocol

from src.domain.entities import JiraTicket


class AcceptanceCriteriaPort(Protocol):
    def generar_criterios(self, ticket: JiraTicket) -> dict:
        """Genera criterios de aceptación en formato Given / When / Then."""
