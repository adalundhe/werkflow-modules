# werkflow-docker

Version `0.4.0`

Asynchronous Docker client, CLI build options, and fluent Dockerfile `Image` builder module for [Werkflow](https://github.com/adalundhe/werkflow).

## Installation

```bash
pip install werkflow-docker
```

## Features

- **Async Docker SDK & CLI Wrapper (`Docker.client` / `DockerClient`):** Async image build, tag, push, pull, login, container lifecycle, and registry operations.
- **Fluent Dockerfile Builder (`Image`):** Programmatically construct, parse (`from_string()`, `from_file()`), query (`layers()`), resolve build args/env vars (`resolve()`), and export (`to_string()`, `to_file()`, `to_memory_file()`, `to_context()`) multi-stage Dockerfiles with typed layer models (`Stage`, `Arg`, `Env`, `Copy`, `Add`, `Run`, `Cmd`, `Entrypoint`, `Expose`, `Label`, `Workdir`, `User`, `Volume`, `Healthcheck`, `Shell`, `StopSignal`, `OnBuild`, and BuildKit mounts).
- **Typed CLI Build Options (`BuildOptions`):** Pydantic v2 validation for `--platform`, `--build-arg`, `--label`, `--secret`, `--cache-from`, `--add-host`, `--no-cache`, `--pull`, `--squash`, and more via `to_string()`.
- **Async Lifecycle:** Supports `async with Docker() as docker:`, `await docker.close()`, and `docker.abort()`.

## Usage

```python
from werkflow_docker import BuildOptions, Docker, Image

image = (
    Image("my-service", tag="1.0.0")
    .stage("python:3.12-slim", alias="builder")
    .workdir("/app")
    .env("PYTHONUNBUFFERED", "1")
    .copy("pyproject.toml", "/app/")
    .run("pip install .")
)

opts = BuildOptions(platform="linux/amd64", no_cache=True)
print(opts.to_string())
print(image.to_string())

async with Docker() as docker:
    loaded = await docker.load_image("./Dockerfile", image_name="my-service")
```

## Dependencies

- `werkflow-core`
- `werkflow-shell`
- `werkflow-system`
- `docker`
- `pydantic`

## Requirements

- Python `>=3.11`
- Local Docker daemon / CLI for build and container operations
