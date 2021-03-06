# fastapi-aiohttp-simple-example [![Python 3.8](https://img.shields.io/badge/python-3.8.9-blue.svg)](https://www.python.org/downloads/release/python-389/) [![build-deploy-prod](https://github.com/eduardomatoss/fastapi-aiohttp-simple-example/actions/workflows/prod-build-deploy.yml/badge.svg)](https://github.com/eduardomatoss/fastapi-aiohttp-simple-example/actions/workflows/prod-build-deploy.yml)

This is an example of a [FastAPI](https://fastapi.tiangolo.com/) project with [aiohttp](https://docs.aiohttp.org/en/stable/)

## Technology and Resources

- [Python 3.8.9](https://www.python.org/downloads/release/python-389/)
- [Pipenv](https://github.com/pypa/pipenv)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Uvicorn](https://github.com/encode/uvicorn)
- [aiohttp](https://github.com/aio-libs/aiohttp)
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

## Commands to help run the project

Command | Docker | Locally | Description
---- | ------- | ------- | -------
install | `make docker/install` | `make local/install` | to install
shell | - | `make local/shell` | to activate the python virtual env using pipenv
tests | `make docker/test` | `make local/test` | to run the unit tests
lint | `make docker/lint` | `make local/lint` | to lint
bandit | `make docker/bandit` | `make local/bandit` | to execute the bandit check
check-packages | `make docker/check-packages` | `make local/check-packages` | to check for packages vulnerabilities
run | `make docker/run` | `make local/run` | to run the project

**Helpful commands**

*Please, check all available commands in the [Makefile](Makefile) for more information*.

## Extras infos

If you use the [vscode](https://code.visualstudio.com/) editor we have some examples of [launch.json](.docs/vscode.md) to speed up your tests
