# Everything-about-Python

- We'll have bunch of commands in a file and we'll handover that file to python interpretor.

### PIP - Preferred Installer Program 

- PIP helps to install the packages that are not already installed by default with python

- Installing a Package :
```bash
python3 -m pip install requests
```

- Installing a specific version of Package :
```bash
python3 -m pip install requests==2.30.1
```

- Installs the current version of the package :
```bash
python3 -m pip install -U requests
# `-U` or `--upgrade`
```

- Uninstalling a Package :
```bash 
python3 -m pip uninstall requests
```

- Listing all the installed packages :
```bash
python3 -m pip list
```

### Virtual Environment : 

- A virtual environment in Python is an isolated directory containing a specific Python interpreter and its own set of installed packages. 

- It provides a dedicated workspace for individual Python projects, preventing conflicts between project dependencies and maintaining a clean system-wide Python installation.

- Command to create a virtual environment :
```bash
python3 -m venv .venv
```

- Activating the Virtual Environment :
```bash
source .venv/bin/activate
```

- Deactivating the virtual environment :
```bash
deactivate
```

**NOTE :** 

1. Once a virtual environment is created, we no more need to use "python3 -m" or "py -m" prefix. We can directly use "pip instal <Package_Name>".

2. We can create a file in which all the packages used will be mentioned in that file. To create that file, run the following command :
```bash
python3 -m pip freeze > requirements.txt
```