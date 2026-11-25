# Versions

The tools, images and libraries FSPY-ESS uses, and the version of each.
Briefs never name versions: when a version matters, a task points here.
**Checked on 10 November 2026** against each project's official release page or package registry. Caddy and PostgreSQL were checked again on **24 November 2026**.

How to read the tables:

- **Pinned** means: use exactly this version. The kit's own files use it, such as `cloudlab/docker-compose.yml`.
- **Course version** means: install this version. A newer patch release (the last number) is fine.
- **Tested** means: the version the course was tested with. Your project's lock file (`uv.lock` or `package-lock.json`) pins the exact version you get.

## On your laptop (Windows)

[`setup/windows.md`](setup/windows.md) installs these.

| Tool | Version | Kind | When | Notes |
|---|---|---|---|---|
| Windows | 11, version 23H2 or newer | minimum | week 1 | Docker Desktop needs 23H2 (build 22631) or newer |
| Git for Windows (Git Bash) | 2.56.0 | course version | week 1 | Any 2.45 or newer works |
| VS Code | the newest | — | week 1 | It updates itself |
| uv | 0.13.7 | course version | week 1 | 0.12 or newer. From uv 0.12, `uv init` makes a packaged `src/` project with no `main.py`; for a flat `main.py` project, use `uv init --no-package --python 3.12 NAME` |
| Python | 3.12.16 | course version | week 1 | Any 3.12 release. Install it with `uv python install 3.12`; uv's Python is the only Python you need |
| Docker Desktop | 4.99.0 | course version | week 1 | The current release, with the WSL 2 engine. Free under the Personal plan for individual learning, and for small businesses with fewer than 250 employees and less than $10 million in yearly revenue |
| WSL | 2.1.5 or newer | minimum | week 1 | Docker Desktop runs on it. Check with `wsl --version`; update with `wsl --update` |
| Node.js | 24.22.2 LTS ("Krypton") | course version | week 6 | v24 or newer. Use the nodejs.org Windows installer and choose v24: `winget install OpenJS.NodeJS.LTS` now gives v26 |
| npm | 11.19.1 | tested | week 6 | Comes with Node.js 24 |

## Cloud lab images

These are pinned in [`cloudlab/docker-compose.yml`](cloudlab/docker-compose.yml). Do not change them in your own copy.

| Service | Image | Kind | Notes |
|---|---|---|---|
| PostgreSQL 16 | `pgvector/pgvector:0.8.7-pg16` | pinned | PostgreSQL 16.15. The same image as the full FSPY course; it also carries the pgvector extension, which this course does not use |
| Redis 7 | `redis:7.4.12-alpine` | pinned | |
| Mailpit | `axllent/mailpit:v1.33.1` | pinned | Catches every email your app sends |

## Images for your capstone's Dockerfiles and Compose files (CP2)

| Use | Image | Kind | Notes |
|---|---|---|---|
| uv inside your API's Dockerfile | `ghcr.io/astral-sh/uv:0.13.7` | pinned | The `<tag>` in `COPY --from=ghcr.io/astral-sh/uv:<tag> /uv /bin/uv` is `0.13.7`, the course's uv version. Built and checked on 24 November 2026 |
| Python services | `python:3.12-slim` (now `python:3.12.16-slim-trixie`) | course version | Both stages of the API's Dockerfile |
| PostgreSQL in your Compose stack | `postgres:16-alpine` (now `postgres:16.16-alpine`) | course version | Checked 24 November 2026 |
| Building the web app | `node:24-alpine` (now `node:24.22.2-alpine`) | course version | The build stage of the web Dockerfile |
| Serving the web app and HTTPS (Caddy 2) | `caddy:2-alpine` (now `caddy:2.11.9-alpine`) | course version | The final stage of the web Dockerfile. Caddy 2.11.9 was released on 5 November 2026; checked 24 November 2026. See [`deploy/`](deploy/README.md) |

## The cloud server (CP2)

| What | Version | Notes |
|---|---|---|
| Server operating system | Ubuntu Server 24.04 LTS | The image in the EC2 console's Quick Start list |
| Docker on the server | the current Docker Engine and Compose plugin | Installed with Docker's script, `get.docker.com`, as [`deploy/README.md`](deploy/README.md) shows |

## Testing and CI

| Tool | Version | Kind | Notes |
|---|---|---|---|
| Playwright | 1.65.0 | course version | The npm package `@playwright/test` (P4 and CP2) |
| act | 0.2.97 | course version | Runs GitHub Actions workflows on your laptop, if Actions does not start (P1). `winget install -e --id nektos.act`; it needs Docker Desktop |

### GitHub Actions (P1)

Use these versions in workflow files, written as `uses: name@version`:

| Action | Version |
|---|---|
| `actions/checkout` | `v7` |
| `actions/setup-python` | `v7` |
| `actions/setup-node` | `v7` |
| `astral-sh/setup-uv` | `v10.3.3` (a full tag: setup-uv no longer publishes a moving `v10` tag) |
| `actions/cache` | `v6` |

Run jobs on `runs-on: ubuntu-latest`.

## Python libraries

Add them with `uv add`, for example `uv add "fastapi==0.162.3"` to pin one.

| Package | Tested | Used in | Notes |
|---|---|---|---|
| `pytest` | 9.2.0 | P1 onwards | |
| `ruff` | 0.17.4 | P1 onwards | Linter and formatter |
| `typer` | 0.29.0 | P1 | |
| `rich` | 15.0.0 | P1 | Comes with Typer |
| `fastapi` | 0.162.3 | P2 onwards | Install as `fastapi[standard]` |
| `uvicorn` | 0.54.0 | P2 onwards | Comes with `fastapi[standard]` |
| `pydantic` | 2.14.3 | P2 onwards | |
| `pydantic-settings` | 2.16.2 | P2 onwards | |
| `sqlalchemy` | 2.1.8 | P2 onwards | The SQLAlchemy 2 style, with `asyncio` |
| `asyncpg` | 0.32.0 | P2 onwards | |
| `alembic` | 1.20.1 | P2 onwards | |
| `httpx` | 0.28.1 | P2 onwards | The test client uses it |
| `pytest-asyncio` | 1.4.1 | P2 onwards | |
| `pyjwt` | 2.15.1 | P2 sign-in | |
| `pwdlib` | 0.3.1 | P2 sign-in | Password hashing, with `pwdlib[argon2]` |
| `email-validator` | 2.3.0 | P2 sign-in | For Pydantic's `EmailStr` |

## npm packages

Add them with `npm install`, for example `npm install zod@4.6.7` to pin one.

| Package | Tested | Used in | Notes |
|---|---|---|---|
| `vite` | 8.3.7 | P3 onwards | `npm create vite@latest` uses `create-vite` 9.3.4; a scripted run needs `--no-interactive` |
| `react`, `react-dom` | 19.3.1 | P3 onwards | |
| `typescript` | 7.0.2 | P3 onwards | Vite's React template asks for `~7.0.2` |
| `@vitejs/plugin-react` | 6.3.0 | P3 onwards | |
| `vitest` | 5.1.0 | P3 onwards | |
| `oxlint` | 1.93.0 | P3 onwards | The linter in Vite's template |
| `react-router` | 8.5.2 | P4 | The version in the P4 starter's lock file; `npm install react-router` gives 8.x, as the P4 briefs say. The declarative API the briefs use (`BrowserRouter`, `Routes`, `NavLink`, `Navigate`) is the same in 7.x |
| `@tanstack/react-query` | 5.107.1 | P4 | |
| `zod` | 4.6.7 | P4 | |
| `@playwright/test` | 1.65.0 | P4 and CP2 | |
| `tailwindcss`, `@tailwindcss/vite` | 4.3.5 | optional | Not in the P4 starter; this course uses plain CSS and no task needs it |
