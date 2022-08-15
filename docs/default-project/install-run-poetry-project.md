# Install + Run Poetry Project

At this point we've generated a default Cookiecutter project, initialized a local repository, and made some minor changes to the project files. In this step we install and run the project using Poetry.

## Install + Run

In PowerShell, `cd` to the Cookiecutter project directory.

```powershell
# Start Poetry shell
poetry shell

# List project dependencies
poetry show

# Install package locally for testing
poetry install

# Run project - should print Hello, World!
poetry run dogg-biscuit

# Update poetry.lock file
poetry update

# Run project - should print Hello, World!
poetry run dogg-biscuit

# If all is well, commit
git add . && git commit -m "poetry update"
```

## Activate a Poetry Project

At some point you'll close PowerShell and exit Poetry. To get back, `cd` to the project directory and run:

```powershell
poetry shell
```
