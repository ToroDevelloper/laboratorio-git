# Scrum + TBD Playbook

## 1. Principios Acordados
1. **Ramas cortas:** Ninguna rama de trabajo vive más de 24 horas.
2. **Main siempre verde:** Mantener la rama principal estable y desplegable es la prioridad absoluta del equipo.
3. **Lotes pequeños:** Pull Requests atómicos para revisiones rápidas.
4. **Desacoplar despliegue de lanzamiento:** Todo código no visible al usuario se integra oculto tras un Feature Flag.
5. **Cero merges sin CI:** Ningún cambio entra a main sin pasar antes por pruebas automáticas en verde.

## 2. Roles Adaptados a TBD + CD
- **Product Owner (PO):** Prioriza por riesgo y tamaño de lote; administra el encendido/apagado de Feature Flags en producción vía ConfigCat; participa en el slicing vertical.
- **Developers:** Ownership total del pipeline de CI/CD; integran código a diario en main; garantizan tests automáticos en verde y monitorean el deploy en Render.
- **Scrum Master:** Facilita la resolución rápida de revisiones de código (<30 min); fomenta cultura sin culpas ante fallas de integración; protege tiempo de mejora del pipeline.

## 3. Reglas de Oro de Integración a main
- Branch Protection obligatorio en `main`.
- Al menos 1 aprobación requerida antes del merge.
- Suite de CI (tests, linter Ruff, build Docker) en estado verde obligatorio.
- Si `main` se rompe, se detienen nuevas tareas hasta corregirlo o hacer rollback inmediato.

---

## 4. Definition of Done (DoD) - Versión Definitiva

Una historia o incremento se considera **DONE** únicamente cuando cumple los criterios en sus 3 dimensiones:

### 🛠️ A. DoD Técnico
- [x] Código revisado mediante Pull Request (o pair/mob programming).
- [x] Pipeline de CI verde obligatorio (pruebas unitarias en Pytest + análisis estático con Ruff).
- [x] Construcción y publicación exitosa de la imagen Docker en GitHub Container Registry (GHCR).
- [x] Feature Toggle configurado e integrado vía ConfigCat (si la funcionalidad no está completa o no es pública).
- [x] No se rompe funcionalidad existente (regresión cero validada por tests automatizados).

### 💼 B. DoD de Negocio
- [x] Criterios de Aceptación (Acceptance Criteria) cumplidos en su totalidad.
- [x] Comportamiento verificable directamente en el entorno de destino (Render).
- [x] El Product Owner conoce el estado del Feature Flag y tiene la potestad de encenderlo/apagarlo.

### 🚀 C. DoD de Despliegue
- [x] Desplegado automáticamente en Render tras el merge a `main`.
- [x] Health check en `/healthz` respondiendo HTTP 200 OK (`{"status": "healthy"}`).
- [x] Logs y monitoreo básico verificados sin excepciones ni errores de arranque.
- [x] Feature Toggle en el estado acordado (OFF por defecto para nuevas funciones).

---

## 5. Checklist de Cierre - Fase 1
- [x] **CI Automatizado y Robusto:** Ruff + Pytest ejecutándose en cada Push y PR.
- [x] **Branch Protection:** Rama `main` protegida contra pushes directos y merges rotos.
- [x] **Empaquetado Docker:** Imágenes generadas automáticamente en GHCR en cada push a `main`.
- [x] **Continuous Deployment (CD):** Auto-deploy configurado y funcionando hacia Render desde `main`.
- [x] **Feature Flags:** Integración de SDK ConfigCat para desacoplar despliegue de lanzamiento.
- [x] **DoD Formalizado:** Criterios técnicos, de negocio y despliegue acordados y documentados.

---

## 6. Adaptación de Ceremonias
- **Daily Scrum:** ¿Qué voy a integrar hoy a main y qué necesito para que sea seguro?
- **Sprint Review:** Demo con base en producción activando/desactivando flags en vivo desde ConfigCat.
- **Sprint Retrospective:** Auditoría de la salud del pipeline, tiempo de ciclo de PRs y disciplina TBD.

## 7. Definition of Ready (DoR) para TBD
Una historia solo ingresa al Sprint Backlog si cumple:
- Sliceada para integrarse a `main` en <= 1 día de desarrollo.
- Criterios de Aceptación verificables en producción o staging tras despliegue.
- Feature Toggle definido (nombre técnico y estado inicial en ConfigCat).
- Sin dependencias externas bloqueantes.
- Mecanismo de validación entendido por todo el equipo.
