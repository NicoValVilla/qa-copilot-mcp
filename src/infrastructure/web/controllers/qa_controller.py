from fastapi import APIRouter, Depends

from src.application.dtos import CasoPruebaDTO, CriterioAceptacionDTO, EsfuerzoQADTO, RiesgosDTO
from src.application.use_cases import (
    AnalizarRiesgosUseCase,
    EstimarEsfuerzoUseCase,
    GenerarCasosPruebaUseCase,
    GenerarCriteriosUseCase,
)
from src.infrastructure.web.controllers.schemas import JiraTicketRequest
from src.infrastructure.web.dependencies import (
    get_criteria_use_case,
    get_effort_use_case,
    get_risk_use_case,
    get_testing_use_case,
)

router = APIRouter(tags=["QA Copilot"])


@router.post("/testing", response_model=CasoPruebaDTO)
def generar_testing(
    request: JiraTicketRequest,
    use_case: GenerarCasosPruebaUseCase = Depends(get_testing_use_case),
) -> CasoPruebaDTO:
    return use_case.execute(request.to_domain())


@router.post("/criteria", response_model=CriterioAceptacionDTO)
def generar_criteria(
    request: JiraTicketRequest,
    use_case: GenerarCriteriosUseCase = Depends(get_criteria_use_case),
) -> CriterioAceptacionDTO:
    return use_case.execute(request.to_domain())


@router.post("/risks", response_model=RiesgosDTO)
def analizar_risks(
    request: JiraTicketRequest,
    use_case: AnalizarRiesgosUseCase = Depends(get_risk_use_case),
) -> RiesgosDTO:
    return use_case.execute(request.to_domain())


@router.post("/effort", response_model=EsfuerzoQADTO)
def estimar_effort(
    request: JiraTicketRequest,
    use_case: EstimarEsfuerzoUseCase = Depends(get_effort_use_case),
) -> EsfuerzoQADTO:
    return use_case.execute(request.to_domain())
