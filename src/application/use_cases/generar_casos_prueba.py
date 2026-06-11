from src.application.dtos import CasoPruebaDTO
from src.domain.entities import JiraTicket
from src.domain.ports import TestingAnalysisPort


class GenerarCasosPruebaUseCase:
    def __init__(self, testing_port: TestingAnalysisPort) -> None:
        self._testing_port = testing_port

    def execute(self, ticket: JiraTicket) -> CasoPruebaDTO:
        result = self._testing_port.generar_casos_prueba(ticket)
        return CasoPruebaDTO.model_validate(result)
