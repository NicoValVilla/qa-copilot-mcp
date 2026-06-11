from typing import Any

from src.domain.entities import JiraTicket


JIRA_TICKET_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "id": {"type": ["string", "null"]},
        "titulo": {"type": "string"},
        "descripcion": {"type": "string"},
        "tipo": {"type": "string"},
    },
    "required": ["titulo", "descripcion", "tipo"],
}


def parse_ticket(payload: dict[str, Any]) -> JiraTicket:
    return JiraTicket.model_validate(payload)


def has_security_context(ticket: JiraTicket) -> bool:
    content = f"{ticket.titulo} {ticket.descripcion}".lower()
    security_keywords = ["auth", "oauth", "login", "sesion", "sesión", "token", "google"]
    return any(keyword in content for keyword in security_keywords)
