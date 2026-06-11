from typing import Any

from src.infrastructure.mcp.tools.common import has_security_context, parse_ticket


def analizar_riesgos(payload: dict[str, Any]) -> dict[str, list[str]]:
    ticket = parse_ticket(payload)

    funcionales = [
        f"El flujo de '{ticket.titulo}' podría no cubrir todos los estados del issue {ticket.tipo}.",
        "Mensajes de error ambiguos pueden dificultar la recuperación del usuario.",
    ]
    integracion = [
        "Dependencias externas pueden responder con latencia o fallas intermitentes.",
        "Cambios en contratos de API pueden romper validaciones o mapeos.",
    ]
    seguridad = [
        "Datos sensibles podrían exponerse en logs o mensajes de error.",
    ]

    if has_security_context(ticket):
        integracion.append("El proveedor Google OAuth puede cambiar permisos, scopes o callbacks.")
        seguridad.extend(
            [
                "Tokens OAuth mal gestionados pueden permitir sesiones inválidas.",
                "Falta de validación del callback puede introducir riesgo de suplantación.",
            ]
        )

    return {
        "riesgos_funcionales": funcionales,
        "riesgos_integracion": integracion,
        "riesgos_seguridad": seguridad,
    }
