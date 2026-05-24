## What is a Virtual Environment?
A virtual environment is an isolated Python environment that lets you install packages for a specific project without affecting your global Python installation. Think of it as a "sandbox" for each project.

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
bash# Save all installed packages to a file
```
pip freeze > requirements.txt
```

### Install all packages from the file (useful for teammates or new machines)
```
pip install -r requirements.txt
```