## What is a Virtual Environment?
A virtual environment is an isolated Python environment that lets you install packages for a specific project without affecting your global Python installation. Think of it as a "sandbox" for each project.

# Python Virtual Environments (venv)

## The Problem They Solve

When all Python packages are installed globally, different projects may require different versions of the same package, leading to dependency conflicts.

### Without `venv`

```text
System Python
├── requests 2.28
├── flask 2.0
└── numpy 1.23

Project A needs flask 2.0 ✅
Project B needs flask 3.0 ❌ CONFLICT
```

Since both projects share the same Python environment, installing a different version of Flask for one project can break the other.

### With `venv`

```text
System Python
├── Project A (.venv)
│   ├── requests 2.28
│   └── flask 2.0
│
└── Project B (.venv)
    ├── requests 2.31
    └── flask 3.0
```

### Benefits

* Each project has its own isolated Python environment.
* Different projects can use different versions of the same package.
* Prevents dependency conflicts.
* Keeps project dependencies organized and reproducible.
* Makes collaboration easier by ensuring consistent environments.

## Key Takeaway

A virtual environment (`venv`) creates an isolated workspace for a Python project, allowing each project to maintain its own Python packages and versions without affecting other projects or the system Python installation.


### macOS
1. Create a Virtual Environment
```
bashpython3 -m venv venv
```

2. Activate it
```
bashsource venv/bin/activate
```

3. You'll see the env name in your terminal prompt:
```
bash(venv) your-mac:project-folder username$
```

4. Deactivate when done
```
bashdeactivate
```

### Windows
1. Create a Virtual Environment
```
cmdpython -m venv venv
```

2. Activate it
Command Prompt:
```
cmdvenv\Scripts\activate
```

3. Deactivate when done
```
cmddeactivate
```

Installing Packages Inside the Virtual Environment
Once activated, use pip normally — packages install only inside the venv:
```
bashpip install requests
pip install flask
```

Saving & Restoring Dependencies
bash# Save all installed packages to a file:
```
pip freeze > requirements.txt
```

Install all packages from the file (useful for teammates or new machines):
```
pip install -r requirements.txt
```