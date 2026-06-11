from pydantic import BaseModel


class CasoPruebaDTO(BaseModel):
    casos_positivos: list[str]
    casos_negativos: list[str]
    casos_borde: list[str]


class CriterioAceptacionDTO(BaseModel):
    criterios: list[str]


class RiesgosDTO(BaseModel):
    riesgos_funcionales: list[str]
    riesgos_integracion: list[str]
    riesgos_seguridad: list[str]


class EsfuerzoQADTO(BaseModel):
    nivel: str
    explicacion: str
