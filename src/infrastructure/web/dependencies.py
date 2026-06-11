from functools import lru_cache
import os

from src.application.use_cases import (
    AnalizarRiesgosUseCase,
    EstimarEsfuerzoUseCase,
    GenerarCasosPruebaUseCase,
    GenerarCriteriosUseCase,
)
from src.infrastructure.mcp import MCPClient, StdioMCPClient, build_mcp_server
from src.infrastructure.mcp.adapters import (
    MCPAcceptanceCriteriaAdapter,
    MCPEffortEstimationAdapter,
    MCPRiskAnalysisAdapter,
    MCPTestingAnalysisAdapter,
)


@lru_cache
def get_mcp_client() -> MCPClient | StdioMCPClient:
    if os.getenv("QA_COPILOT_MCP_MODE", "local").lower() in {"real", "stdio"}:
        return StdioMCPClient.from_environment()
    return MCPClient(build_mcp_server())


def get_testing_use_case() -> GenerarCasosPruebaUseCase:
    return GenerarCasosPruebaUseCase(MCPTestingAnalysisAdapter(get_mcp_client()))


def get_criteria_use_case() -> GenerarCriteriosUseCase:
    return GenerarCriteriosUseCase(MCPAcceptanceCriteriaAdapter(get_mcp_client()))


def get_risk_use_case() -> AnalizarRiesgosUseCase:
    return AnalizarRiesgosUseCase(MCPRiskAnalysisAdapter(get_mcp_client()))


def get_effort_use_case() -> EstimarEsfuerzoUseCase:
    return EstimarEsfuerzoUseCase(MCPEffortEstimationAdapter(get_mcp_client()))
