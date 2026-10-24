# EveryNumber — Activación y alquiler de números con estados de pedido explícitos

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg">
    <img alt="Un pedido aprobado obtiene un número, consulta el código dentro de un límite y solo se cobra cuando el código llega." src="assets/hero-light.svg" width="100%">
  </picture>
</p>

<p align="center">
  <a href="https://cursor.com/en/install-mcp?name=everyinfra&config=eyJ1cmwiOiJodHRwczovL2FwaS5ldmVyeWluZnJhLmNvbS9tY3AiLCJoZWFkZXJzIjp7IkF1dGhvcml6YXRpb24iOiJCZWFyZXIgPEFQSSBLZXk%2BIn19"><img src="https://img.shields.io/badge/Instalar_en_Cursor-2F363D?style=for-the-badge&logo=cursor&logoColor=white" alt="Instalar en Cursor"></a>
  <a href="https://vscode.dev/redirect/mcp/install?name=everyinfra&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fapi.everyinfra.com%2Fmcp%22%2C%22headers%22%3A%7B%22Authorization%22%3A%22Bearer%20%3CAPI%20Key%3E%22%7D%7D"><img src="https://img.shields.io/badge/Instalar_en_VS_Code-0065A9?style=for-the-badge&logo=githubcopilot&logoColor=white" alt="Instalar en VS Code"></a>
  <a href="https://github.com/everyinfra/everyinfra-agent-plugins/blob/main/i18n/README.es.md#claude-code"><img src="https://img.shields.io/badge/Claude_Code-un_comando-B4532A?style=for-the-badge&logo=claude&logoColor=white" alt="Claude Code: un comando"></a>
  <a href="https://github.com/everyinfra/everyinfra-agent-plugins/blob/main/i18n/README.es.md#codex"><img src="https://img.shields.io/badge/Codex-un_comando-2F363D?style=for-the-badge" alt="Codex: un comando"></a>
</p>

<p align="center">
  <a href="https://github.com/everyinfra/everyinfra-agent-plugins/stargazers"><img src="https://img.shields.io/github/stars/everyinfra/everyinfra-agent-plugins?style=social" alt="GitHub stars of everyinfra-agent-plugins"></a>
  &nbsp;<b>Dale una estrella al repo principal y recibe $1 de saldo.</b> <a href="https://everyinfra.com/es/docs?utm_source=github&utm_medium=readme&utm_campaign=everynumber-plugin&utm_content=star_line#quickstart">Cómo reclamarlo →</a>
</p>

<p align="center"><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <b>Español</b></p>

> [!TIP]
> **Este repositorio contiene una sola skill: EveryNumber.** El plugin completo de EveryInfra (10 skills, el servidor MCP remoto en `https://api.everyinfra.com/mcp` y la configuración para Claude Code, Codex, Cursor y VS Code) está en **[everyinfra/everyinfra-agent-plugins](https://github.com/everyinfra/everyinfra-agent-plugins)**. Los botones de arriba conectan el servidor MCP; la instalación del plugin en cada entorno está en el repo principal.

> [!NOTE]
> **Los pedidos de EveryNumber no están disponibles por ahora.** La skill sigue consultando primero los catálogos en vivo e indica qué se puede pedir antes de hacer ningún pedido.

[Configuración](docs/setup.md) · [Flujo de trabajo](docs/workflow.md) · [Prompts](examples/prompts.md) · [Referencia de capacidades](docs/reference.md) · [Documentación de la API](https://api.everyinfra.com/docs) <sub>(en inglés)</sub>

EveryNumber es una skill independiente de EveryInfra para activar y alquilar números de teléfono autorizados a través de REST. Descubre el inventario actual, conserva la cotización del pedido, pone límite a la consulta del código y distingue la liquidación de una activación de la compra de un alquiler.

Úsala para verificaciones que tienes permiso para hacer. Ninguna de estas skills da permiso para crear cuentas ni para saltarse las reglas de un servicio.

## Qué puedes hacer

- Comparar la disponibilidad actual por país y producto antes de pedir un número.
- Seguir un pedido de activación con un plan de consulta y cancelación acotado.
- Explicar en qué se diferencia un alquiler de una activación antes de comprometer dinero.

## Instalación

Es un paquete independiente con una sola skill y un flujo de trabajo **REST**; no es un servicio nuevo. Necesita un entorno de agente compatible y el acceso configurado que describe la [guía de configuración](docs/setup.md). Validar el paquete en local no demuestra que la API esté disponible.

Revisa el contenido del repositorio y luego instálalo en Codex. Estos comandos añaden un catálogo respaldado por GitHub, no un aval de ningún marketplace oficial:

```bash
codex plugin marketplace add everyinfra/everynumber-plugin
codex plugin add everynumber@everynumber-plugin
```

Para una copia local, cambia la fuente del primer comando por `.`. La [guía de configuración](docs/setup.md) también cubre Claude Code y la conexión al servicio, que va aparte.

Con el acceso configurado, prueba:

> Revisa las opciones de activación actuales para el país y el producto que te indico. No pidas ningún número.

Este primer prompt solo inspecciona o prepara. Revisa cualquier operación de pago o efecto externo antes de seguir.

## Cómo funciona

1. Lee `GET /api/v1/sms/catalog`; para alquileres, `GET /api/v1/sms/rental/catalog`.
2. Confirma el país, el producto o el plazo del alquiler y el gasto antes de hacer el pedido.
3. Para una activación, llama a `POST /api/v1/sms/number` y conserva el ID del pedido y la cotización fijada.
4. Consulta `GET /api/v1/sms/code/{order_id}` dentro de un límite explícito de tiempo y de peticiones; informa del estado de liquidación real.
5. Cancela una activación sin usar con `POST /api/v1/sms/cancel/{order_id}` solo si está permitido. El alquiler (`POST /api/v1/sms/rental`) es un pedido de pago distinto y esta skill no lo cancela ni lo renueva.

**Un buen resultado:** una comparación de disponibilidad, un pedido con estado autorizado o un resultado entregado con seguridad. Conserva las condiciones cotizadas y no deduzcas la liquidación solo porque se asignó un número.

## Límites y seguridad

- Solo REST; la disponibilidad y los precios salen de los catálogos y respuestas de pedido actuales.
- La activación se liquida según el contrato de obtención del código; el alquiler se cobra al hacer el pedido.
- Nada de cancelaciones o renovaciones automáticas de alquileres, consultas sin límite ni códigos de un solo uso en archivos o registros.

El paquete trae una sola skill: no concede permisos ni registra una segunda conexión MCP. No pongas credenciales en prompts, archivos del repositorio, capturas ni registros compartidos. Descubrir, ejecutar, cobrar y obtener un resultado externo final son estados distintos. Consulta la [política de seguridad](SECURITY.md).

## Preguntas frecuentes y validación

Las preguntas frecuentes, la comprobación sin conexión (`python3 scripts/validate.py`) y la guía para contribuir están en el [README en inglés](README.md#frequently-asked-questions).

Mantenido por [EveryInfra](https://everyinfra.com/es?utm_source=github&utm_medium=readme&utm_campaign=everynumber-plugin&utm_content=footer). Licencia [Apache-2.0](LICENSE).
