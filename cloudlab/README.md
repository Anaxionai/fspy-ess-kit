# Cloud lab

The cloud lab runs the course's databases on your laptop, in Docker Desktop. Nothing here costs money, and nothing leaves your laptop.

It is one Compose file, `docker-compose.yml`, with one profile (a named group of services), `core`. You use it from P2 (week 4) to the end of the course.

## Before you start

- Docker Desktop is running, with the WSL 2 backend. `setup/windows.md` in this kit shows how to install it.
- You use Git Bash in the VS Code terminal for every command.
- Go to this folder first. Every command in this file runs from here:

```bash
cd ~/fspy-ess-kit/cloudlab
docker compose version
```

The second command prints `Docker Compose version v2...`. If it prints an error, start Docker Desktop and wait until it says "Engine running".

## What `core` starts

| Service | What it is | Used in |
|---|---|---|
| `postgres` | PostgreSQL 16, the database for RailSeat and your capstone | P2, P4, CP1, CP2 |
| `redis` | Redis 7, a fast key-value store | only if your capstone needs a cache |
| `mailpit` | Mailpit, which catches every email your app sends | only if your app sends email |

## Start the lab

```bash
docker compose --profile core up -d
```

The first start downloads the images once. On a slow connection this can take 10 minutes.

Check that it runs:

```bash
docker compose --profile core ps
```

Every line should say `Up`, and after a few seconds `postgres` and `redis` also say `(healthy)`. The containers are named `cloudlab-<service>-1`: `cloudlab-postgres-1`, `cloudlab-redis-1` and `cloudlab-mailpit-1`.

## Stop the lab

| To stop | Command |
|---|---|
| The lab, keeping its data | `docker compose --profile core down` |
| One service | `docker compose --profile core stop redis` |
| The same service again | `docker compose --profile core start redis` |

Always name the profile. `docker compose down` on its own stops nothing here, because every service belongs to the `core` profile.

## Reset the lab (delete its data)

```bash
docker compose --profile core down -v
```

The `-v` flag deletes the volumes (storage that Docker keeps between runs). PostgreSQL and Redis keep their data after a plain `down`; after `down -v` they start empty. Mailpit keeps nothing.

## Ports and passwords

These passwords work only on your laptop. Never use them on a real server: the deploy in `deploy/README.md` makes new ones.

| Service | Address from your laptop | User and password |
|---|---|---|
| PostgreSQL 16 | `postgresql://railseat:railseat@localhost:5432/railseat` | user `railseat`, password `railseat`, database `railseat` |
| Redis 7 | `redis://localhost:6379/0` | none |
| Mailpit SMTP | `localhost:1025` | any user name and password, or none; no TLS |
| Mailpit web page | http://localhost:8025 | none |

From Python with SQLAlchemy and asyncpg, the address is `postgresql+asyncpg://railseat:railseat@localhost:5432/railseat`.

### More than one database

RailSeat's tests use a second database, `railseat_test`, and your capstone gets its own. Make one with `createdb` inside the container:

```bash
docker exec cloudlab-postgres-1 createdb -U railseat railseat_test
docker exec cloudlab-postgres-1 psql -U railseat -l
```

The second command lists every database. Open a SQL prompt with `docker exec -it cloudlab-postgres-1 psql -U railseat -d railseat`, and leave it with `\q`.

## RAM advice for 8 GB laptops

The whole lab is small: about 50 MB with the services idle (PostgreSQL 35 MB, Redis 5 MB, Mailpit 10 MB). Your editor, browser and own app need far more.

- Stop the lab when you finish for the day: `docker compose --profile core down`.
- Check live use with `docker stats --no-stream`.
- Docker Desktop's total memory is capped in `.wslconfig` (see `setup/windows.md`, Step 9).
- In the capstone you run your own Compose file too. Stop the lab first if your own file starts its own PostgreSQL on port 5432.

## Reaching the lab from your own containers

Inside a container, `localhost` is the container itself, not your laptop. Use `host.docker.internal` instead, and add this to the service in your own `compose.yaml`:

```yaml
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

For example, an API container reaches the lab's PostgreSQL at `host.docker.internal:5432`.

## Git Bash and paths inside containers

Git Bash changes any argument that starts with `/` into a Windows path. That breaks a Docker command that names a path inside a container. Put `MSYS_NO_PATHCONV=1` in front of that one command:

```bash
MSYS_NO_PATHCONV=1 docker exec cloudlab-postgres-1 ls /var/lib/postgresql/data
```

Commands with no such path need nothing extra, for example `docker compose --profile core ps`. Never `export` the variable for the whole terminal: it breaks other commands, such as `python ~/script.py`.

## Troubleshooting

- **`port is already allocated`** or **`address already in use`**: another program uses that port. Find it with `docker ps --format "table {{.Names}}\t{{.Ports}}"`. A PostgreSQL installed on Windows also takes port 5432: stop it in the Windows Services app.
- **A service is not `Up`** or says `unhealthy`: read its last log lines, for example `docker compose --profile core logs --tail 30 postgres`.
- **PostgreSQL rejects the password `railseat`**: the password is set only when the volume is first made. Reset it with `docker compose --profile core down -v`. This deletes the data.
- **`docker compose down` did nothing**: name the profile: `docker compose --profile core down`.
- **The laptop is slow**: run `docker stats --no-stream`, and stop what you are not using.
- **`Cannot connect to the Docker daemon`**: start Docker Desktop and wait until it says "Engine running".

## Image versions

The images are pinned in `docker-compose.yml`, and listed in the kit's `VERSIONS.md`:

| Service | Image |
|---|---|
| PostgreSQL | `pgvector/pgvector:0.8.7-pg16` (PostgreSQL 16.15) |
| Redis | `redis:7.4.12-alpine` |
| Mailpit | `axllent/mailpit:v1.33.1` |
