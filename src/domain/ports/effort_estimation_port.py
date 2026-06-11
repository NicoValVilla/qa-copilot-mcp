from typing import Protocol

from src.domain.entities import JiraTicket


class EffortEstimationPort(Protocol):
    def estimar_esfuerzo(self, ticket: JiraTicket) -> dict:
        """Estima esfuerzo QA y explica la razón."""
