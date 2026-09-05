Markdown
# ⚡ DevPulse CLI

> Herramienta interactiva de terminal para monitorizar métricas del sistema, puertos en uso y contenedores Docker en tiempo real.

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)
[![Node Version](https://img.shields.io/badge/node-%3E%3D18.0.0-blue.svg)](https://nodejs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 📝 Descripción General

**DevPulse CLI** es un monitor de rendimiento en tiempo real basado en terminal (TUI) diseñado para entornos de desarrollo local y servidores Linux/macOS. Proporciona visibilidad inmediata sobre la carga de CPU, consumo de memoria, mapeo de procesos a puertos de red y estadísticas de contenedores Docker activos, evitando la sobrecarga de paneles web pesados.

---

## 📋 Requisitos Previos

Antes de configurar y ejecutar el proyecto, asegúrate de tener instalado:

- **Node.js**: `>= 18.0.0`
- **Gestor de paquetes**: `npm` `>= 9.x` (o `pnpm` / `yarn`)
- **Docker Engine**: `>= 20.10.x` *(opcional, solo requerido para métricas de contenedores)*
- **Sistema Operativo**: Linux (Debian, Ubuntu, Fedora, Arch) o macOS

---

## 🛠️ Instalación y Configuración del Entorno Local

Sigue estos pasos en orden para levantar el entorno de desarrollo:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/devpulse-cli.git](https://github.com/tu-usuario/devpulse-cli.git)
   cd devpulse-cli
Instalar dependencias del proyecto:

Bash
npm install
Configurar variables de entorno:
Copia la plantilla base y ajusta los valores necesarios:

Bash
cp .env.example .env
Variables configurables en .env:

Fragmento de código
DEVPULSE_INTERVAL=2000              # Frecuencia de muestreo en ms
DEVPULSE_ALERT_CPU_THRESHOLD=85     # Umbral (%) para alerta visual de CPU
DEVPULSE_ALERT_MEM_THRESHOLD=90     # Umbral (%) para alerta visual de RAM
DEVPULSE_DOCKER_SOCKET=/var/run/docker.sock # Ruta al socket de Docker
💻 Guía de Ejecución
Scripts disponibles definidos en el entorno:

Bash
# Iniciar en modo desarrollo con recarga automática
npm run dev

# Compilar TypeScript a JavaScript de producción
npm run build

# Ejecutar el binario compilado en modo producción
npm run start

# Ejecutar la suite completa de pruebas unitarias
npm test

# Analizar la calidad y estilo del código
npm run lint

# Formatear archivos con Prettier
npm run format
Ejemplos de uso directo
Bash
# Lanzar dashboard interactivo estándar
node dist/index.js

# Monitorear a un intervalo rápido de 1 segundo
node dist/index.js --interval 1000

# Inspeccionar exclusivamente el daemon de Docker
node dist/index.js docker

# Auditar procesos que escuchan en puertos específicos
node dist/index.js ports --check 3000,8080,5432
📁 Estructura del Proyecto
Resumen de la arquitectura modular del código fuente:

Plaintext
devpulse-cli/
├── src/
│   ├── collectors/       # Módulos de recolección de datos (CPU, RAM, red, Docker)
│   ├── ui/               # Renderizado del dashboard TUI en terminal
│   ├── config/           # Carga y validación de variables de entorno y flags
│   ├── utils/            # Helpers de formateo de datos, timers y procesos PID
│   └── index.ts          # Punto de entrada de la aplicación CLI
├── tests/                # Pruebas unitarias e integración con Jest
├── .env.example          # Plantilla base de configuración de variables
├── .gitignore            # Exclusiones de Git
├── package.json          # Metadatos, scripts y dependencias
├── tsconfig.json         # Configuración del compilador de TypeScript
└── README.md             # Documentación principal del repositorio
🤝 Contribuciones
Para mantener la consistencia del proyecto:

Revisa nuestra guía detallada en CONTRIBUTING.md.

Crea una rama descriptiva (git checkout -b docs/update-readme o git checkout -b feat/add-metric).

Sigue la convención de Conventional Commits.

Asegúrate de que npm test y npm run lint pasen exitosamente antes de abrir un Pull Request.

📄 Licencia
Este proyecto está bajo los términos de la Licencia MIT.
