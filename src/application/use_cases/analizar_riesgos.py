from src.application.dtos import RiesgosDTO
from src.domain.entities import JiraTicket
from src.domain.ports import RiskAnalysisPort


class AnalizarRiesgosUseCase:
    def __init__(self, risk_port: RiskAnalysisPort) -> None:
        self._risk_port = risk_port

    def execute(self, ticket: JiraTicket) -> RiesgosDTO:
        result = self._risk_port.analizar_riesgos(ticket)
        return RiesgosDTO.model_validate(result)
