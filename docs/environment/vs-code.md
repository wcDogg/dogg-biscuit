# Configure Editor

While these notes are specific to VS Code, other editors will have equivalent settings & behaviors.

## VS Code settings.json

1. Open Settings: `Ctrl+,`.
2. Open `settings.json` - File icon in upper-right.
3. Add / modify / save:

```json
// Use UNIX-style line endings (line feed, lf)
"files.eol": "\n",

// Make things easier
"terminal.integrated.copyOnSelection": true,

// Add terminal profiles
"terminal.integrated.profiles.windows": {
    "Git Bash": {
        "path": ["C:\\Program Files\\Git\\bin\\bash.exe"],
        "source": "Git Bash",
        "icon": "terminal-bash"
    },
    "PowerShell": {
        "path": ["C:\\Programs\\PowerShell\\pwsh.exe"],
        "source": "PowerShell",
        "icon": "terminal-PowerShell"
    },
}

// Set Git Bash as the default terminal
"terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
```

## VS Code & Pylance

With a `file.py` open in VS Code, the current Python interpreter is displayed in the bottom-right corner. Each Poetry project has it's own virtual environment with it's own interpreter - `/Scripts/python.exe`. When editing in VS Code, get Pylance to work by selecting this interpreter.

## VS Code & PowerShell

Up until now, I've written local scripts that I run in VS Code via the integrated Git Bash terminal provided by Git for Windows.

The tools in a Cookiecutter project are run from the command line - PowerShell. My first thought was to use VS Code's integrated PowerShell the same way I use bash. Annoyingly, I encountered issues I didn't see a need to sort through. Instead, I use VS Code and PowerShell separately - and I prefer it :)

## VS Code Source Control

If you already work with VS Code and GitHub, you're probably using the VS Code Source Control panel to commit and push your changes. As you begin doing things in PowerShell, you'll notice:

- While VS Code will register much of what you do in PowerShell, there can be a lag and sometimes you need to refresh.
- The Source Control panel will usually register a `git commit` from PowerShell. It will auto-refresh and display the 'Synch Changes' button.
- The Source Control panel is spotty at registering `git push`. It may continue to display the 'Synch Changes' button until the 'Refresh' icon is clicked.
- VS Code displays the current branch in the bottom-right corner. Using `git checkout branch` and then changing focus to VS Code will cause VS Code to register the branch change as seen in the corner.
