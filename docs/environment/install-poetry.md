# Install Poetry

[Poetry](https://python-poetry.org/) is a Python packaging + dependency management framework. At the project level, Poetry provides the isolation of a virtual environment - replacing `venv` or `dotenv`.

## Depreciated

`get-poetry.py` is depreciated. The new instructions are here:

- https://python-poetry.org/docs/master/#insthttps://github.com/wcDogg/windows/blob/main/git-github.mdalling-with-the-official-installer

## Steps

The documentation is a muddle. What ultimately worked for me was:

1. Download this file as `install-poetry.py` to an easy location: https://install.python-poetry.org/.
2. In PowerShell:

```powershell
# Install
python D:\HyperPy\hpermodern-python\install-poetry.py

# Uninstall
python D:\HyperPy\hpermodern-python\install-poetry.py --uninstall
```

3. You'll see a message like below. See [Add to $PATH](add-to-path.md) for how to do this:

```
To get started you need Poetry's bin directory (C:\Users\wcd\AppData\Roaming\Python\Scripts) in your `PATH` environment variable.
```

4. Test: `poetry --version`.
