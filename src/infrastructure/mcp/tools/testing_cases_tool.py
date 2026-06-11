from typing import Any

from src.infrastructure.mcp.tools.common import has_security_context, parse_ticket


def generar_casos_prueba(payload: dict[str, Any]) -> dict[str, list[str]]:
    ticket = parse_ticket(payload)

    positivos = [
        f"Validar que una persona usuaria pueda completar correctamente: {ticket.titulo}.",
        f"Confirmar que el flujo principal del issue tipo {ticket.tipo} actualiza la interfaz esperada.",
    ]
    negativos = [
        "Validar comportamiento cuando faltan datos obligatorios.",
        "Confirmar que entradas inválidas muestran mensajes claros y no rompen el flujo.",
    ]
    borde = [
        "Validar el flujo con datos mínimos permitidos.",
        "Validar reintentos y estados de espera ante respuestas lentas.",
    ]

    if has_security_context(ticket):
        positivos.append("Validar inicio de sesión exitoso con una cuenta Google válida.")
        negativos.append("Validar rechazo cuando el proveedor OAuth cancela o niega permisos.")
        borde.append("Validar expiración de token y renovación de sesión.")

    return {
        "casos_positivos": positivos,
        "casos_negativos": negativos,
        "casos_borde": borde,
    }
