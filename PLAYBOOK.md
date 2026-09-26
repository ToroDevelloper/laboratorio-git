# Scrum + TBD Playbook

## 1. Principios Acordados
1. **Ramas cortas:** Ninguna rama de trabajo vive más de 24 horas[cite: 2].
2. **Main siempre verde:** Mantener la rama principal estable y desplegable es la prioridad absoluta del equipo[cite: 2].
3. **Lotes pequeños:** Pull Requests atómicos para revisiones rápidas[cite: 2].
4. **Desacoplar despliegue de lanzamiento:** Todo código no visible al usuario se integra oculto tras un Feature Flag[cite: 2].
5. **Cero merges sin CI:** Ningún cambio entra a main sin pasar antes por pruebas automáticas en verde[cite: 2].

## 2. Roles Adaptados a TBD + CD
- **Product Owner:** Prioriza por riesgo y tamaño de lote; administra el encendido/apagado de Feature Flags en producción; participa en el slicing vertical[cite: 2].
- **Developers:** Ownership total del pipeline de CI/CD; integran código a diario en main; garantizan tests automáticos en verde[cite: 2].
- **Scrum Master:** Facilita la resolución rápida de revisiones de código; fomenta cultura sin culpas ante fallas de integración; protege tiempo de mejora del pipeline[cite: 2].

## 3. Reglas de Oro de Integración a main
- Branch Protection obligatorio en `main`[cite: 2].
- Al menos 1 aprobación requerida antes del merge[cite: 2].
- Suite de CI (tests, linter, build) en estado verde obligatorio[cite: 2].
- Si `main` se rompe, se detienen nuevas tareas hasta corregirlo o hacer rollback inmediato[cite: 2].

## 4. Definition of Done (DoD)
- [ ] Pruebas unitarias e integración añadidas y pasando[cite: 2].
- [ ] Pipeline de CI aprobado en la rama[cite: 2].
- [ ] Code Review aprobada[cite: 2].
- [ ] Merge completado a `main`[cite: 2].
- [ ] Feature Flag configurado y apagado por defecto en ConfigCat (para funciones no públicas)[cite: 2, 7].
- [ ] Criterios de aceptación verificables directamente en entorno real/producción[cite: 2].

## 5. Adaptación de Ceremonias
- **Daily Scrum:** ¿Qué voy a integrar hoy a main y qué necesito para que sea seguro?[cite: 2]
- **Sprint Review:** Demo con base en producción activando/desactivando flags en vivo[cite: 2].
- **Sprint Retrospective:** Auditoría de la salud del pipeline, tiempo de vida de PRs y disciplina TBD[cite: 2].

## 6. Decisiones Pendientes
- Convención de nombres y permisos en ConfigCat[cite: 2, 7].
- Seguimiento de métricas de flujo (tiempo de ciclo de PRs y tasa de fallo en CI)[cite: 2].
- Optimización de caché y tiempos de ejecución del pipeline[cite: 11].
