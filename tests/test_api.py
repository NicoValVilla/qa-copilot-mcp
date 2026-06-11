import pytest

pytest.importorskip("httpx")

from fastapi.testclient import TestClient

from src.main import create_app


client = TestClient(create_app())


def test_effort_endpoint_returns_high_for_oauth_story() -> None:
    response = client.post(
        "/effort",
        json={
            "titulo": "Agregar autenticación con Google",
            "descripcion": "Los usuarios deben poder iniciar sesión usando OAuth2 con Google.",
            "tipo": "Story",
        },
    )

    assert response.status_code == 200
    assert response.json()["nivel"] == "Alto"
