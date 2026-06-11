# 🎯 Guía de Presentación - QA Copilot MCP

## 📊 Cómo Usar la Presentación

### Abrir la Presentación

1. Abre el archivo `PRESENTACIÓN.html` en tu navegador web
2. O accede vía: `File → Open → PRESENTACIÓN.html`
3. Presiona **F** para pantalla completa
4. Presiona **S** para ver notas del presentador (si aplica)

### Navegar por las Diapositivas

| Tecla | Acción |
|-------|--------|
| **→** o **Espacio** | Siguiente diapositiva |
| **←** | Diapositiva anterior |
| **Arriba/Abajo** | Navegar verticalmente (si hay subdivisiones) |
| **F** | Pantalla completa |
| **Esc** | Salir de pantalla completa |
| **O** | Vista general de todas las diapositivas |
| **N** | Notas del presentador |

---

## ⏱️ Estructura de 8 Minutos

La presentación está diseñada para ~8 minutos de exposición:

| Minuto | Diapositivas | Contenido |
|--------|-------------|----------|
| 0-1 | 1 | Portada y contexto |
| 1-2 | 2-3 | El problema y qué es MCP |
| 2-4 | 4-6 | Arquitectura hexagonal, capas, estructura |
| 4-5.5 | 7-13 | Herramientas, flujo, endpoints, instalación |
| 5.5-7 | 14-16 | Ventajas, tecnologías, validación |
| 7-8 | 17-20 | Lecciones, conclusiones, demostración |
| 8+ | 21-23 | Preguntas y cierre |

---

## 🗣️ Script Sugerido por Diapositiva

### Diapositiva 1: Portada (30 segundos)

```
"Buenos días/tardes. Presento QA Copilot MCP, un proyecto educativo que 
demuestra cómo implementar Model Context Protocol con Arquitectura Hexagonal.
```

### Diapositivas 2-3: El Problema y MCP (1 minuto)

```
"Las APIs personalizadas son un problema: cada servicio define su propio estándar,
sin estandarización, el código es frágil. 

MCP resuelve esto con un protocolo estándar JSON-RPC que permite a clientes 
(IDEs, LLMs) interactuar de forma segura con servidores que exponen herramientas.
```

### Diapositivas 4-6: Arquitectura (1.5 minutos)

```
"Usamos Arquitectura Hexagonal: separamos responsabilidades en 4 capas.
El Web layer recibe solicitudes, Application orquesta casos de uso, 
Domain contiene la lógica, Infrastructure implementa con MCP.

La clave es que los casos de uso NO conocen MCP ni FastAPI - solo dependen 
de Puertos. Esto permite reemplazar la implementación sin afectar la lógica.
```

### Diapositivas 7-8: Herramientas (1 minuto)

```
"Tenemos 4 herramientas MCP principales:
- Generar casos de prueba
- Generar criterios BDD (Given/When/Then)
- Analizar riesgos
- Estimar esfuerzo QA

Todas reciben un ticket Jira y generan artefactos de QA automáticamente.
```

### Diapositivas 9-13: Flujo, API, Instalación (1.5 minutos)

```
"El flujo es: usuario → dashboard → API REST → casos de uso → puerto → 
adaptador MCP → cliente MCP → servidor MCP → tool → resultado.

Tenemos 4 endpoints REST principales: /testing, /criteria, /risks, /effort.

Para instalar: clonar repositorio, crear entorno virtual, pip install, 
y ejecutar uvicorn.
```

### Diapositivas 14-16: Ventajas, Tecnologías, Validación (1 minuto)

```
"MCP tiene ventajas claras: estandarización, tipado estricto, seguridad, 
documentación auto-descubierta.

Usamos FastAPI, Pydantic, pytest, Python 3.11+.

El proyecto alcanza 86/100 puntos: arquitectura impecable, 4 tools funcionales,
API REST, dashboard web, pruebas, documentación completa.
```

### Diapositivas 17-20: Lecciones, Conclusiones, Demo (1.5 minutos)

```
"Aprendimos que la Arquitectura Hexagonal proporciona máxima flexibilidad.
Puertos y Adaptadores permiten cambiar implementación sin afectar lógica.
MCP simplifica integración LLM-herramientas.

Conclusión: MCP es revolucionario por estandarización, seguridad, reutilización
y escalabilidad.

Ahora veremos una demostración en vivo [mostrar video o ejecutar aplicación].
```

### Diapositivas 21-23: Preguntas y Cierre (1 minuto)

```
"¿Preguntas sobre MCP, la arquitectura o la implementación?

[Responder preguntas]

Gracias por su atención. El código está disponible en GitHub.
```

---

## 📹 Integrar Video de Demostración

Para incluir un video de demostración (máx. 2 minutos) de forma profesional:

### Opción 1: Mostrar en Pantalla Completa
1. Prepara un video MP4 con la demostración
2. Antes de la diapositiva 20, reproduce el video en pantalla completa
3. O integra un enlace en la diapositiva

### Opción 2: Demo en Vivo
1. Abre una terminal con la aplicación ejecutándose
2. Accede a `http://localhost:8000`
3. Muestra el dashboard
4. Llena un formulario de ejemplo
5. Ejecuta análisis y muestra los resultados

---

## 🎨 Consejos de Presentación

### ✅ Haz:
- Habla claro y a ritmo moderado (no muy rápido)
- Haz contacto visual con la audiencia
- Pausa después de puntos importantes
- Usa la presentación como guía, no como script
- Resalta los conceptos clave (Puertos, Adaptadores, JSON-RPC)
- Muestra la demostración con confianza

### ❌ Evita:
- Leer directamente de las diapositivas
- Movimiento excesivo o distracciones
- Hablar muy rápido por nervios
- Minimizar el valor educativo (enfatiza el aprendizaje)
- Saltarte explicaciones (todos no tienen contexto MCP)

---

## 📋 Checklist Antes de Presentar

- [ ] Probaste la presentación en tu navegador
- [ ] La aplicación está lista para demo en vivo
- [ ] Tienes acceso a internet (para cargar Reveal.js)
- [ ] La terminal está lista para mostrar la instalación
- [ ] El video de demostración está preparado
- [ ] Tienes el README impreso o disponible como respaldo
- [ ] Probaste el micrófono y proyector
- [ ] Ensayaste al menos una vez el flujo completo

---

## 🔧 Solucionar Problemas

### La presentación no carga en el navegador
- Asegúrate que tienes conexión a internet (Reveal.js está en CDN)
- Intenta con otro navegador
- Verifica que el archivo HTML está en la carpeta correcta

### Las diapositivas se ven pequeñas
- Presiona **+** para zoom in
- O ajusta la resolución de pantalla

### Necesito agregar más información
- Abre el archivo HTML en un editor de texto
- Agrega nuevas `<section>` con el contenido
- Guarda y recarga en el navegador

### La presentación no tiene audio
- Las diapositivas no incluyen audio
- Tú proporcionas el audio hablando

---

## 📞 Soporte

Si tienes dudas sobre:
- **Contenido técnico:** Ver `docs/arquitectura.md` y `README.md`
- **Cómo ejecutar la app:** Ver sección "Instalación" en README
- **Estructura de carpetas:** Ver `ESTRUCTURA_PROYECTO.txt` (si existe)

---

## 🎓 Lecturas Recomendadas Antes de Presentar

1. **Model Context Protocol (MCP)**
   - https://modelcontextprotocol.io
   - Léelo una vez para entender conceptos

2. **Arquitectura Hexagonal**
   - Eirik Mørland's blog: "Hexagonal Architecture"
   - Robert C. Martin's "Clean Architecture"

3. **JSON-RPC 2.0**
   - https://www.jsonrpc.org/specification
   - Entender el protocolo te ayuda a explicar MCP

---

## ⏰ Timing Aproximado por Sección

- **Portada:** 30 seg
- **Problema + MCP:** 60 seg
- **Arquitectura:** 90 seg
- **Herramientas + Flujo:** 90 seg
- **API + Instalación:** 60 seg
- **Ventajas + Tech + Validación:** 60 seg
- **Lecciones + Conclusiones:** 60 seg
- **Demostración:** 120 seg
- **Q&A + Cierre:** 60 seg

**Total: ~8 minutos** (ajustable según preguntas)

---

**¡Listo para presentar! 🎉**
