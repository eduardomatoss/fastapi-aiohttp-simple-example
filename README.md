# fastapi-aiohttp-simple-example

This is an example project of using fastapi with aiohttp

## Technology and Resources

- [Python 3.8.0](https://www.python.org/downloads/release/python-380/)
- [Pipenv](https://github.com/pypa/pipenv)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Uvicorn](https://github.com/encode/uvicorn)
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

### How to Install

```
make local/install
```

### How to Build

```
make docker/build
```

### How to Run

```
make local/run

make docker/run
```

### How to Test

```
make local/test

make docker/test
```

### How to lint

`make docker/lint` or `make local/lint` to lint

`make docker/bandit` or `make local/bandit` to execute the bandit check

`make docker/check-packages` or `make local/check-packages` to check for packages vulnerabilities

**Helpful commands**

*Please, check all available commands in the [Makefile](Makefile) for more information*.

### Extras infos

If you use the [vscode](https://code.visualstudio.com/) editor we have some examples of [launch.json](.docs/vscode.md) to speed up your tests
