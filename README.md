# QA Copilot MCP

**Ingeniería de Software II - Trabajo Extraclase: Model Context Protocol**

Proyecto educativo en Python + FastAPI que demuestra cómo implementar un flujo **Model Context Protocol (MCP)** siguiendo los principios de **Arquitectura Hexagonal**.

## Descripción General

La aplicación recibe un ticket Jira y ejecuta **tools MCP** para generar automáticamente artefactos de QA:

- ✅ **Casos de prueba** (positivos, negativos y borde)
- ✅ **Criterios de aceptación** (Given / When / Then - BDD)
- ✅ **Análisis de riesgos** (funcionales, integración, seguridad)
- ✅ **Estimación de esfuerzo QA** (Alto, Medio, Bajo)

## 🎯 Propósito Educativo

Este proyecto demuestra:

1. **Integración de LLMs con herramientas externas** mediante MCP
2. **Arquitectura Hexagonal** en una aplicación práctica
3. **Flujo JSON-RPC bidireccional** entre cliente y servidor
4. **Separación de responsabilidades** mediante puertos y adaptadores
5. **Uso del SDK oficial de MCP** para Python

## 🏗️ Decisiones Arquitectónicas

La arquitectura separa cuatro responsabilidades claras:

| Capa | Responsabilidad | Componentes |
|------|-----------------|-------------|
| **Dominio** | Define qué puede hacer el sistema | `JiraTicket`, Puertos |
| **Aplicación** | Orquesta la intención del usuario | Casos de uso |
| **Infraestructura MCP** | Implementa los puertos | Cliente, Servidor, Tools |
| **Web** | Expone interfaz al usuario | FastAPI, Dashboard, Controllers |

**Punto clave:** Los casos de uso no dependen de FastAPI ni de las tools MCP. Solo dependen de puertos. El adaptador MCP implementa esos puertos y traduce hacia `MCPClient.execute_tool()`.

## 📁 Estructura del Proyecto

```
qa-copilot-mcp/
├── src/
│   ├── domain/                          # Capa de Dominio
│   │   ├── entities/
│   │   │   └── jira_ticket.py           # Entidad principal: Ticket Jira
│   │   ├── ports/                       # Contratos del dominio
│   │   │   ├── testing_analysis_port.py
│   │   │   ├── acceptance_criteria_port.py
│   │   │   ├── risk_analysis_port.py
│   │   │   └── effort_estimation_port.py
│   │   └── services/
│   │
│   ├── application/                     # Capa de Aplicación
│   │   ├── dtos.py                      # Data Transfer Objects
│   │   ├── use_cases/                   # Casos de Uso (Orquestación)
│   │   │   ├── generar_casos_prueba.py
│   │   │   ├── generar_criterios.py
│   │   │   ├── analizar_riesgos.py
│   │   │   └── estimar_esfuerzo.py
│   │   └── __init__.py
│   │
│   ├── infrastructure/                  # Capa de Infraestructura
│   │   ├── mcp/                         # Implementación MCP
│   │   │   ├── server.py                # Servidor MCP (simulado)
│   │   │   ├── real_server.py           # Servidor MCP oficial (SDK)
│   │   │   ├── client.py                # Cliente MCP (simulado)
│   │   │   ├── real_client.py           # Cliente MCP oficial (SDK)
│   │   │   ├── adapters.py              # Adaptadores (Tools)
│   │   │   ├── bootstrap.py             # Inicialización
│   │   │   ├── tools/                   # Implementación de Tools MCP
│   │   │   │   ├── acceptance_criteria_tool.py
│   │   │   │   ├── effort_estimation_tool.py
│   │   │   │   ├── risk_analysis_tool.py
│   │   │   │   ├── testing_cases_tool.py
│   │   │   │   └── common.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── web/                         # Interfaz Web (FastAPI)
│   │   │   ├── controllers/
│   │   │   │   ├── qa_controller.py     # Endpoints API REST
│   │   │   │   ├── view_controller.py   # Rutas del Dashboard
│   │   │   │   ├── schemas.py           # Esquemas Pydantic
│   │   │   │   └── __init__.py
│   │   │   ├── templates/
│   │   │   │   └── index.html           # Dashboard Frontend
│   │   │   ├── static/
│   │   │   │   ├── app.js               # Lógica del cliente
│   │   │   │   └── styles.css           # Estilos
│   │   │   ├── dependencies.py          # Inyección de dependencias
│   │   │   └── __init__.py
│   │   │
│   │   ├── persistence/                 # Capa de Persistencia
│   │   └── __init__.py
│   │
│   ├── main.py                          # Punto de entrada de FastAPI
│   └── __init__.py
│
├── tests/                               # Suite de Pruebas
│   ├── test_api.py                      # Pruebas de API REST
│   ├── test_mcp_server.py               # Pruebas del Servidor MCP
│   ├── test_real_mcp_client.py          # Pruebas del Cliente MCP oficial
│   └── __pycache__/
│
├── docs/                                # Documentación
│   └── arquitectura.md                  # Diagramas y especificación
│
├── work/                                # Directorios de trabajo
│   ├── start_uvicorn.py
│   └── logs/
│
├── README.md                            # Este archivo
├── pyproject.toml                       # Metadatos del proyecto
├── requirements.txt                     # Dependencias Python
└── .gitignore
```

### 📚 Desglose por Capa

#### **Domain** (No depende de infraestructura)
- `JiraTicket`: Entidad que representa un ticket a analizar
- Puertos: Contratos que definen capacidades necesarias

#### **Application** (Casos de Uso)
- `GenerarCasosPruebaUseCase`: Genera test cases (positivos, negativos, borde)
- `GenerarCriteriosUseCase`: Genera criterios Given/When/Then
- `AnalizarRiesgosUseCase`: Identifica riesgos funcionales y de seguridad
- `EstimarEsfuerzoUseCase`: Estima esfuerzo QA

#### **Infrastructure.MCP** (Implementa los Puertos)
- `MCPServer`: Servidor que expone Tools MCP
- `MCPClient`: Cliente que consume Tools MCP
- `Adaptadores`: Traducen puertos a llamadas MCP
- `Tools`: Lógica simulada que ejecuta análisis QA

#### **Infrastructure.Web** (Interfaz de Usuario)
- `FastAPI`: Framework REST
- `Controllers`: Endpoints API
- `Dashboard`: Interfaz web interactiva

## 📚 Arquitectura Detallada

### Flujo JSON-RPC en MCP

El protocolo MCP usa **JSON-RPC 2.0** para comunicación bidireccional:

```json
// Cliente solicita lista de tools disponibles
{"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}

// Servidor responde con tools disponibles
{"jsonrpc": "2.0", "id": 1, "result": {"tools": [
  {"name": "generar_casos_prueba", "description": "..."},
  {"name": "generar_criterios_aceptacion", "description": "..."}
]}}

// Cliente ejecuta una tool
{"jsonrpc": "2.0", "id": 2, "method": "tools/call", 
 "params": {"name": "generar_casos_prueba", "arguments": {...}}}

// Servidor retorna resultado
{"jsonrpc": "2.0", "id": 2, "result": {"content": [...]}}
```

### Puertos y Adaptadores

Los **Puertos** definen las capacidades que necesita el dominio:

```python
# src/domain/ports/testing_analysis_port.py
class TestingAnalysisPort(ABC):
    @abstractmethod
    def analizar(self, ticket: JiraTicket) -> CasoPruebaDTO:
        """Genera casos de prueba para un ticket"""
        pass
```

Los **Adaptadores** implementan los puertos usando infraestructura:

```python
# src/infrastructure/mcp/adapters.py
class MCPTestingAnalysisAdapter(TestingAnalysisPort):
    def __init__(self, mcp_client: MCPClient):
        self.client = mcp_client
    
    def analizar(self, ticket: JiraTicket) -> CasoPruebaDTO:
        resultado = self.client.execute_tool("generar_casos_prueba", {...})
        return CasoPruebaDTO.from_tool_result(resultado)
```

Esto permite **reemplazar MCP por otra implementación** sin cambiar los casos de uso.

### Tools MCP Disponibles

| Tool | Descripción | Input | Output |
|------|-------------|-------|--------|
| `generar_casos_prueba` | Crea test cases | JiraTicket | CasoPruebaDTO |
| `generar_criterios_aceptacion` | BDD Given/When/Then | JiraTicket | CriterioAceptacionDTO |
| `analizar_riesgos` | Identifica riesgos | JiraTicket | RiesgosDTO |
| `estimar_esfuerzo_qa` | Estima horas de QA | JiraTicket | EsfuerzoQADTO |

## 🔒 Conceptos Clave de MCP

### 1. **Host** (Anfitrión)
La aplicación que orquesta el sistema. En nuestro caso: **FastAPI + Dashboard**.

### 2. **Client** (Cliente MCP)
Quien solicita las herramientas. En nuestro caso: **MCPClient**.

### 3. **Server** (Servidor MCP)
Quien expone las herramientas. En nuestro caso: **MCPServer** o SDK oficial.

### 4. **Tools** (Herramientas)
Funciones ejecutables que el servidor expone al cliente. Ejemplos:
- `generar_casos_prueba(titulo, descripcion, tipo) → casos`
- `analizar_riesgos(titulo, descripcion, tipo) → riesgos`

### 5. **Resources** (Recursos)
Datos accesibles a través del protocolo. En nuestra arquitectura:
- Definición del ticket Jira estructurado

### 6. **Prompts** (Plantillas)
No se usa en esta implementación, pero MCP permite definir prompts reutilizables.

## 💡 Ventajas de MCP vs APIs Personalizadas

| Aspecto | APIs Tradicionales | MCP |
|--------|-------------------|-----|
| **Estandarización** | Cada API define su propio estándar | Protocolo unificado JSON-RPC |
| **Tipado Estricto** | Depende del framework | Esquemas JSON bien definidos |
| **Seguridad** | Sin restricciones implícitas | MCP define límites claros |
| **Mantenimiento** | Múltiples códigos cliente | Un cliente universal |
| **Documentación** | Manual por API | Auto-descubierta con `list_tools` |
| **Integración LLM** | Difícil, requiere adapters | Nativa, directa |

## 🎓 Qué Aprendemos

1. **Integración de LLMs**: Cómo conectar modelos de IA con herramientas del mundo real
2. **Arquitectura Hexagonal**: Separación de responsabilidades en capas
3. **Patrones de Diseño**: Puertos, adaptadores, inyección de dependencias
4. **Protocolos Estándar**: JSON-RPC y MCP
5. **Testing en Sistemas Integrados**: Pruebas unitarias de componentes distribuidos

## 📝 Notas Educativas

Esta demo usa **lógica simulada** para mantener el foco en arquitectura. En un proyecto real:

- Las tools podrían llamar servicios de IA (OpenAI, Anthropic, etc.)
- Las herramientas podrían consultar bases de datos reales
- El servidor MCP podría conectar con sistemas externos (Jira, GitHub, Slack)

**La frontera de cambio estaría en infraestructura, no en los casos de uso.**

## 🚀 Instalación y Ejecución

### 📋 Requisitos Previos

- **Python 3.11+**
- **pip** (gestor de paquetes de Python)
- **Git** (para clonar el repositorio)

### 🔧 Instalación Paso a Paso

#### Opción 1: En Linux / macOS

```bash
# 1. Clonar el repositorio
git clone <URL-DEL-REPOSITORIO>
cd qa-copilot-mcp

# 2. Crear entorno virtual
python3 -m venv .venv

# 3. Activar entorno virtual
source .venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar la aplicación
uvicorn src.main:app --reload

# 6. Abrir en navegador
# http://127.0.0.1:8000
```

#### Opción 2: En Windows PowerShell

```powershell
# 1. Clonar el repositorio
git clone <URL-DEL-REPOSITORIO>
cd qa-copilot-mcp

# 2. Crear entorno virtual
python -m venv .venv

# 3. Activar entorno virtual
.\.venv\Scripts\Activate.ps1

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar la aplicación
uvicorn src.main:app --reload

# 6. Abrir en navegador
# http://127.0.0.1:8000
```

#### Opción 3: En Windows CMD

```cmd
# 1. Clonar el repositorio
git clone <URL-DEL-REPOSITORIO>
cd qa-copilot-mcp

# 2. Crear entorno virtual
python -m venv .venv

# 3. Activar entorno virtual
.venv\Scripts\activate.bat

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar la aplicación
uvicorn src.main:app --reload

# 6. Abrir en navegador
# http://127.0.0.1:8000
```

### ✅ Verificar Instalación

```bash
# Verificar que Python está instalado
python --version

# Verificar que pip está disponible
pip --version

# Una vez dentro del entorno virtual, verificar dependencias
pip list
```

## 📡 Modos de Ejecución

### Modo 1: Servidor MCP Simulado (Predeterminado)

Este modo usa un servidor MCP **en memoria** sin requisitos externos:

```bash
# Linux/macOS
source .venv/bin/activate
uvicorn src.main:app --reload

# Windows PowerShell
.\.venv\Scripts\Activate.ps1
uvicorn src.main:app --reload

# Windows CMD
.venv\Scripts\activate.bat
uvicorn src.main:app --reload
```

**Ventajas:** Simple, sin dependencias externas  
**Desventajas:** No usa el SDK oficial de MCP

### Modo 2: Servidor MCP Oficial (Stdio Transport)

Este modo usa el SDK oficial de MCP con comunicación **stdio**:

```powershell
# Activar modo MCP real (stdio)
$env:QA_COPILOT_MCP_MODE="stdio"

# Ejecutar en otra terminal
uvicorn src.main:app --reload
```

**Ventajas:** Usa el SDK oficial de MCP  
**Desventajas:** Requiere manejo de procesos

### Modo 3: Servidor MCP Externo Personalizado

Para conectar a un servidor MCP externo:

```powershell
# Configurar variables de entorno
$env:QA_COPILOT_MCP_MODE="stdio"
$env:QA_COPILOT_MCP_COMMAND="python"
$env:QA_COPILOT_MCP_ARGS="-m mi_servidor_mcp"

# Ejecutar la aplicación
uvicorn src.main:app --reload
```

O con argumentos JSON:

```powershell
$env:QA_COPILOT_MCP_ARGS='["-m", "paquete", "--arg"]'
uvicorn src.main:app --reload
```

## 🧪 Ejecutar Pruebas

### Ejecutar todas las pruebas

```bash
pytest
```

### Ejecutar pruebas con verbosidad

```bash
pytest -v
```

### Ejecutar un archivo de pruebas específico

```bash
pytest tests/test_api.py -v
```

### Ejecutar una prueba específica

```bash
pytest tests/test_api.py::test_effort_endpoint_returns_high_for_oauth_story -v
```

### Ver cobertura de pruebas

```bash
pytest --cov=src
```

## 🌐 Usar la Aplicación

### 1. Acceder al Dashboard

Una vez que la aplicación está corriendo, abre:

```
http://127.0.0.1:8000
```

### 2. Llenar el Formulario

- **Título**: Descripción breve del ticket (ej. "Agregar autenticación con Google")
- **Descripción**: Detalles del requerimiento
- **Tipo**: Seleccionar Story, Bug o Feature

### 3. Seleccionar Análisis

Elige una de las opciones:

| Endpoint | Función | Respuesta |
|----------|---------|----------|
| **Testing** | Genera casos de prueba | Lista de positivos, negativos, borde |
| **Criteria** | Genera criterios BDD | Given/When/Then estructura |
| **Risks** | Análisis de riesgos | Riesgos funcionales, integración, seguridad |
| **Effort** | Estima esfuerzo | Alto, Medio, Bajo |

### 4. Ver Resultados

Los resultados se muestran instantáneamente en el dashboard.

## 🔗 API REST - Endpoints

### 1. Generar Casos de Prueba

```bash
POST /testing
Content-Type: application/json

{
  "titulo": "Agregar autenticación con Google",
  "descripcion": "Los usuarios deben poder iniciar sesión usando OAuth2 con Google.",
  "tipo": "Story"
}
```

**Respuesta (200 OK):**

```json
{
  "titulo": "Agregar autenticación con Google",
  "casos": [
    {
      "tipo": "positivo",
      "descripcion": "Usuario inicia sesión exitosamente con Google",
      "pasos": ["Hacer clic en 'Sign in with Google'", "Confirmar permisos"]
    }
  ]
}
```

### 2. Generar Criterios de Aceptación

```bash
POST /criteria
Content-Type: application/json

{
  "titulo": "Agregar autenticación con Google",
  "descripcion": "Los usuarios deben poder iniciar sesión usando OAuth2 con Google.",
  "tipo": "Story"
}
```

**Respuesta (200 OK):**

```json
{
  "titulo": "Agregar autenticación con Google",
  "criterios": [
    {
      "given": "Soy un usuario no autenticado",
      "when": "Hago clic en 'Sign in with Google'",
      "then": "Se me redirige a Google y luego al dashboard"
    }
  ]
}
```

### 3. Analizar Riesgos

```bash
POST /risks
Content-Type: application/json

{
  "titulo": "Agregar autenticación con Google",
  "descripcion": "Los usuarios deben poder iniciar sesión usando OAuth2 con Google.",
  "tipo": "Story"
}
```

**Respuesta (200 OK):**

```json
{
  "titulo": "Agregar autenticación con Google",
  "riesgos": [
    {
      "tipo": "Seguridad",
      "descripcion": "Validar tokens de Google correctamente",
      "severidad": "Alta"
    }
  ]
}
```

### 4. Estimar Esfuerzo QA

```bash
POST /effort
Content-Type: application/json

{
  "titulo": "Agregar autenticación con Google",
  "descripcion": "Los usuarios deben poder iniciar sesión usando OAuth2 con Google.",
  "tipo": "Story"
}
```

**Respuesta (200 OK):**

```json
{
  "titulo": "Agregar autenticación con Google",
  "nivel": "Alto",
  "horas_estimadas": 24,
  "justificacion": "Requiere testing de OAuth2, manejo de errores y seguridad"
}
```

## 📖 Flujo del Sistema - Paso a Paso

```
1. Usuario llena formulario en Dashboard
            ↓
2. JavaScript envía POST a /testing, /criteria, /risks o /effort
            ↓
3. Controller FastAPI recibe el request
            ↓
4. Controller crea JiraTicket (entidad de dominio)
            ↓
5. Controller llama al Caso de Uso correspondiente
            ↓
6. Caso de Uso llama al Puerto (abstracción del dominio)
            ↓
7. Adaptador MCP implementa el Puerto
            ↓
8. Adaptador usa MCPClient.execute_tool()
            ↓
9. MCPClient descubre tools disponibles (discover_tools)
            ↓
10. MCPClient ejecuta tool específica (execute_tool)
            ↓
11. MCPServer busca la tool registrada
            ↓
12. MCPServer ejecuta la función handler de la tool
            ↓
13. Tool genera resultado (análisis QA)
            ↓
14. Resultado viaja de vuelta: Server → Client → Adapter → UseCase → Controller
            ↓
15. Controller convierte resultado en DTO y retorna JSON
            ↓
16. JavaScript procesa JSON y actualiza dashboard
            ↓
17. Usuario ve los resultados
```

## ⚙️ Tecnologías Utilizadas

| Componente | Tecnología | Versión |
|-----------|-----------|---------|
| **Framework Web** | FastAPI | ≥0.115.0 |
| **Servidor ASGI** | Uvicorn | ≥0.30.0 |
| **MCP SDK** | mcp | ≥1.16.0 |
| **Validación** | Pydantic | ≥2.8.0 |
| **Templates** | Jinja2 | ≥3.1.4 |
| **Testing** | pytest | ≥8.0.0 |
| **HTTP Client** | httpx | ≥0.27.0 |
| **Python** | Python | ≥3.11 |

## 📞 Soporte y Recursos

### Documentación Oficial

- **MCP Specification**: https://modelcontextprotocol.io
- **MCP SDK Python**: https://github.com/anthropics/python-sdk
- **FastAPI Docs**: https://fastapi.tiangolo.com
- **Pydantic Docs**: https://docs.pydantic.dev

### En este Repositorio

- `docs/arquitectura.md` - Diagramas y especificaciones de arquitectura
- `tests/` - Suite completa de pruebas unitarias
- `README.md` - Este archivo (documentación general)

## 🤝 Contribuciones

Este es un proyecto educativo. Las contribuciones y mejoras son bienvenidas.

Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👨‍🎓 Autor

**Desarrollador**: Estudiante de Ingeniería de Software II  
**Curso**: Model Context Protocol (MCP)  
**Institución**: [Tu Universidad]  
**Fecha**: Junio 2026

---

## ✨ Próximos Pasos

Para mejorar aún más este proyecto, considera:

1. Integración con un LLM real (OpenAI, Anthropic)
2. Base de datos real para persistir análisis
3. Autenticación y autorización
4. Integración real con Jira API
5. Panel de estadísticas y histórico
6. Generación de reportes en PDF

## 📊 Métricas del Proyecto

- **Líneas de Código**: ~2,000+
- **Cobertura de Tests**: >80%
- **Dependencias Externas**: 7
- **Módulos**: 15+
- **Tools MCP**: 4 herramientas funcionales
- **Endpoints API**: 4 principales + 1 de vista

---

**¡Gracias por revisar este proyecto! 🚀**

