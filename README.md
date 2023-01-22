
## Configuración sugerida en vscode

```sh
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}\\inventory\\manage.py",
            "python": "${workspaceFolder}\\env_project\\Scripts\\python.exe",
            "envFile": "${workspaceFolder}\\.env",
            "args": [
                "runserver",
                // "--noreload",
                "0.0.0.0:8000",
            ],
            "django": true,
            "justMyCode": true
        }
    ]
}
```