from pydantic import BaseModel, Field

from src.domain.entities import JiraTicket


class JiraTicketRequest(BaseModel):
    id: str | None = Field(default=None)
    titulo: str = Field(min_length=3)
    descripcion: str = Field(min_length=5)
    tipo: str = Field(min_length=2)

    def to_domain(self) -> JiraTicket:
        return JiraTicket.model_validate(self.model_dump())
