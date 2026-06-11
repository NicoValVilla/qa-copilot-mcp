from typing import Any

from src.infrastructure.mcp.tools.common import has_security_context, parse_ticket


def estimar_esfuerzo_qa(payload: dict[str, Any]) -> dict[str, str]:
    ticket = parse_ticket(payload)
    text_size = len(ticket.descripcion.split())

    if has_security_context(ticket):
        return {
            "nivel": "Alto",
            "explicacion": "Incluye autenticación o seguridad, por lo que requiere pruebas funcionales, integración, sesiones y escenarios negativos.",
        }

    if text_size > 35:
        return {
            "nivel": "Medio",
            "explicacion": "La descripción contiene varias reglas o detalles, por lo que requiere una matriz de escenarios moderada.",
        }

    return {
        "nivel": "Bajo",
        "explicacion": "El alcance parece acotado y puede cubrirse con pocos escenarios funcionales.",
    }
