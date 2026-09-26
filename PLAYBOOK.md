# Scrum + TBD Playbook

## 1. Principios Acordados
1. **Ramas cortas:** Ninguna rama de trabajo vive más de 24 horas.
2. **Main siempre verde:** Mantener la rama principal estable y desplegable es la prioridad absoluta del equipo.
3. **Lotes pequeños:** Pull Requests atómicos para revisiones rápidas.
4. **Desacoplar despliegue de lanzamiento:** Todo código no visible al usuario se integra oculto tras un Feature Flag.
5. **Cero merges sin CI:** Ningún cambio entra a main sin pasar antes por pruebas automáticas en verde.

## 2. Roles Adaptados a TBD + CD
- **Product Owner:** Prioriza por riesgo y tamaño de lote; administra el encendido/apagado de Feature Flags en producción; participa en el slicing vertical.
- **Developers:** Ownership total del pipeline de CI/CD; integran código a diario en main; garantizan tests automáticos en verde.
- **Scrum Master:** Facilita la resolución rápida de revisiones de código; fomenta cultura sin culpas ante fallas de integración; protege tiempo de mejora del pipeline.

## 3. Reglas de Oro de Integración a main
- Branch Protection obligatorio en `main`.
- Al menos 1 aprobación requerida antes del merge.
- Suite de CI (tests, linter, build) en estado verde obligatorio.
- Si `main` se rompe, se detienen nuevas tareas hasta corregirlo o hacer rollback inmediato.

## 4. Definition of Done (DoD)
- [ ] Pruebas unitarias e integración añadidas y pasando
- [ ] Pipeline de CI aprobado en la rama.
- [ ] Code Review aprobada.
- [ ] Merge completado a `main`.
- [ ] Feature Flag configurado y apagado por defecto en ConfigCat (para funciones no públicas).
- [ ] Criterios de aceptación verificables directamente en entorno real/producción.

## 5. Adaptación de Ceremonias
- **Daily Scrum:** ¿Qué voy a integrar hoy a main y qué necesito para que sea seguro?
- **Sprint Review:** Demo con base en producción activando/desactivando flags en vivo.
- **Sprint Retrospective:** Auditoría de la salud del pipeline, tiempo de vida de PRs y disciplina TBD.

## 6. Decisiones Pendientes
- Convención de nombres y permisos en ConfigCat.
- Seguimiento de métricas de flujo (tiempo de ciclo de PRs y tasa de fallo en CI).
- Optimización de caché y tiempos de ejecución del pipeline.

## 7. Definition of Ready (DoR) para TBD
Una historia solo ingresa al Sprint Backlog si cumple:
- Sliceada para integrarse a `main` en <= 1 día de desarrollo.
- Criterios de Aceptación verificables en producción o staging tras despliegue.
- Feature Toggle definido (nombre técnico y estado inicial).
- Sin dependencias externas bloqueantes.
- Mecanismo de validación entendido por todo el equipo.

## 8. Acuerdos de Planificación de Sprint (Flujo Continuo)
- **Sprint Goal orientado a TBD:** Redactar separando lo que estará activo para el usuario de lo que quedará integrado bajo toggle.
- **Priorización:** El primer ítem del Sprint Backlog debe poder integrarse a `main` entre el Día 1 y el Día 2.
- **Gestión de Capacidad:** Se reserva capacidad diaria para Code Reviews (< 30 min) y resolución inmediata de alertas del pipeline de CI.

## 9. Acciones concretas para el próximo Sprint
1. Toda historia nueva debe evaluarse con el semáforo de 4 criterios (Tamaño, Verticalidad, Toggle, Validación) antes de entrar a Planning.
2. Si una tarea excede 1 día de desarrollo sin integrarse a `main`, se detiene y se re-slicea en la Daily.
