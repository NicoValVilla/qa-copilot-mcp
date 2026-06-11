from typing import Any

from mcp.server.fastmcp import FastMCP

from src.infrastructure.mcp.tools import (
    analizar_riesgos as analizar_riesgos_local,
    estimar_esfuerzo_qa as estimar_esfuerzo_qa_local,
    generar_casos_prueba as generar_casos_prueba_local,
    generar_criterios_aceptacion as generar_criterios_aceptacion_local,
)


mcp = FastMCP("QA Copilot MCP")


def _payload(titulo: str, descripcion: str, tipo: str, id: str | None = None) -> dict[str, Any]:
    return {
        "id": id,
        "titulo": titulo,
        "descripcion": descripcion,
        "tipo": tipo,
    }


@mcp.tool()
def generar_casos_prueba(
    titulo: str,
    descripcion: str,
    tipo: str,
    id: str | None = None,
) -> dict[str, list[str]]:
    """Genera casos positivos, negativos y borde desde un ticket Jira."""
    return generar_casos_prueba_local(_payload(titulo, descripcion, tipo, id))


@mcp.tool()
def generar_criterios_aceptacion(
    titulo: str,
    descripcion: str,
    tipo: str,
    id: str | None = None,
) -> dict[str, list[str]]:
    """Genera criterios Given / When / Then desde un ticket Jira."""
    return generar_criterios_aceptacion_local(_payload(titulo, descripcion, tipo, id))


@mcp.tool()
def analizar_riesgos(
    titulo: str,
    descripcion: str,
    tipo: str,
    id: str | None = None,
) -> dict[str, list[str]]:
    """Analiza riesgos funcionales, de integracion y seguridad."""
    return analizar_riesgos_local(_payload(titulo, descripcion, tipo, id))


@mcp.tool()
def estimar_esfuerzo_qa(
    titulo: str,
    descripcion: str,
    tipo: str,
    id: str | None = None,
) -> dict[str, str]:
    """Estima esfuerzo QA como Bajo, Medio o Alto."""
    return estimar_esfuerzo_qa_local(_payload(titulo, descripcion, tipo, id))


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
