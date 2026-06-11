from typing import Any

from src.infrastructure.mcp.tools.common import has_security_context, parse_ticket


def generar_criterios_aceptacion(payload: dict[str, Any]) -> dict[str, list[str]]:
    ticket = parse_ticket(payload)

    criterios = [
        (
            f"Given que existe un usuario autorizado, When ejecuta la funcionalidad "
            f"'{ticket.titulo}', Then el sistema completa el flujo esperado."
        ),
        (
            "Given que el usuario ingresa información inválida, When intenta continuar, "
            "Then el sistema muestra validaciones comprensibles."
        ),
    ]

    if has_security_context(ticket):
        criterios.append(
            "Given que el usuario selecciona Google como proveedor, When Google confirma "
            "la identidad, Then el sistema crea una sesión segura."
        )

    return {"criterios": criterios}
