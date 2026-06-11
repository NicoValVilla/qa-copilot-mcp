from src.application.dtos import EsfuerzoQADTO
from src.domain.entities import JiraTicket
from src.domain.ports import EffortEstimationPort


class EstimarEsfuerzoUseCase:
    def __init__(self, effort_port: EffortEstimationPort) -> None:
        self._effort_port = effort_port

    def execute(self, ticket: JiraTicket) -> EsfuerzoQADTO:
        result = self._effort_port.estimar_esfuerzo(ticket)
        return EsfuerzoQADTO.model_validate(result)
