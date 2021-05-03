# fastapi-aiohttp-simple-example

This is an example project of using fastapi with aiohttp

## Technology and Resources

- [Python 3.8.0](https://www.python.org/downloads/release/python-380/)
- [Pipenv](https://github.com/pypa/pipenv)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Uvicorn](https://github.com/encode/uvicorn)
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
