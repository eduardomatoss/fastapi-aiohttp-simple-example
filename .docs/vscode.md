# Debug Code using VSCODE Editor

**Example:**

``` json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "fastapi-aiohttp-simple-example",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/run.py",
            "console": "integratedTerminal",
        }
    ]
}
```

**Example:**

``` json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "run:application",
                "--host",
                "0.0.0.0",
                "--workers",
                "4"
            ],
            "jinja": true
        }
    ]
}
```