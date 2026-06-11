# Arquitectura Hexagonal en QA Copilot MCP

## Regla Principal

Las dependencias apuntan hacia adentro:

```text
Web -> Application -> Domain
MCP Adapter -> Application/Domain contracts
Domain -> no depende de infraestructura
```

## Capas

### Domain

Contiene `JiraTicket` y los puertos. Esta capa define el lenguaje central del negocio QA.

### Application

Contiene los casos de uso. Cada caso expresa una acción concreta:

- `GenerarCasosPruebaUseCase`
- `GenerarCriteriosUseCase`
- `AnalizarRiesgosUseCase`
- `EstimarEsfuerzoUseCase`

### Infrastructure MCP

Simula el patrón MCP:

- `MCPServer.register_tool()`
- `MCPServer.list_tools()`
- `MCPServer.call_tool()`
- `MCPClient.discover_tools()`
- `MCPClient.execute_tool()`

### Web

Expone FastAPI y un dashboard moderno. Es un adaptador de entrada, no contiene reglas de negocio.

## Flujo Detallado

```mermaid
sequenceDiagram
  participant U as Usuario
  participant W as Web Controller
  participant UC as Use Case
  participant A as MCP Adapter
  participant C as MCP Client
  participant S as MCP Server
  participant T as Tool MCP

  U->>W: POST /testing con JiraTicket
  W->>UC: execute(ticket)
  UC->>A: generar_casos_prueba(ticket)
  A->>C: execute_tool("generar_casos_prueba", payload)
  C->>S: list_tools()
  C->>S: call_tool(name, payload)
  S->>T: handler(payload)
  T-->>S: resultado QA
  S-->>C: resultado QA
  C-->>A: resultado QA
  A-->>UC: resultado QA
  UC-->>W: DTO
  W-->>U: JSON
```
