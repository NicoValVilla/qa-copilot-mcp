from pydantic import BaseModel, Field


class JiraTicket(BaseModel):
    """Entidad de dominio que representa la información mínima de un issue Jira."""

    id: str | None = Field(default=None, description="Identificador Jira opcional.")
    titulo: str = Field(min_length=3, description="Resumen o título del issue.")
    descripcion: str = Field(min_length=5, description="Descripción funcional del issue.")
    tipo: str = Field(min_length=2, description="Tipo de issue: Story, Bug, Task, etc.")
