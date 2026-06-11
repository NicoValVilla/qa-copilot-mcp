from src.application.dtos import CriterioAceptacionDTO
from src.domain.entities import JiraTicket
from src.domain.ports import AcceptanceCriteriaPort


class GenerarCriteriosUseCase:
    def __init__(self, criteria_port: AcceptanceCriteriaPort) -> None:
        self._criteria_port = criteria_port

    def execute(self, ticket: JiraTicket) -> CriterioAceptacionDTO:
        result = self._criteria_port.generar_criterios(ticket)
        return CriterioAceptacionDTO.model_validate(result)
