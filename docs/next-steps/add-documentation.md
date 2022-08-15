# Add Documentation

See [External Services](../default-project/external-services.md)

Each time you push commits to GitHub, the project documentation is automatically compiled on [Read the Docs](https://readthedocs.org). This process auto-generates documentation from the repository's README and docstrings in your code. You can - and probably should - add some additional content.

**Read the Docs**

- [Read the Docs](https://readthedocs.org) > User menu > My Projects > Import a Project
- Locate repository and click its `+` button.
- Project Details = defaults
- Versions = latest (defaults)
- Click Build Version

Builds + subsequent updates take a few minutes to generate, but stick around and get familiar with the results.

## Build + Theme

The documentation for a Cookiecutter project:

- Is compiled by [Sphinx](https://www.sphinx-doc.org/en/master/index.html).
- Defaults to the Read the Docs[Furo Theme](https://pradyunsg.me/furo/)

## Languages

Content can be written in:

- [CommonMark Markdown Flavor](https://commonmark.org/)
- [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

This project uses [MyST - Markedly Structure Text Parser](https://myst-parser.readthedocs.io/en/latest/). MyST lets you author in Markdown + leverage reStructuredText features like TOC.

## Content Organization + TOC

Each theme seems to approach TOC options differently and I had a hard time getting the dropdowns working. Here's what worked for me:

- Organize content using subdirectories that equate to categories or chapters.
- Each subdirectory needs an `index.md` with a `toctree`.
- The Markdown for a subdirectory `index.md` looks like this:

## Fenced Code Blocks

To add syntax highlighting to [fenced code blocks](https://spec.commonmark.org/0.30/#fenced-code-blocks), add the [programing language]() immediately after the opening backticks. Here's a Python example:

````
```python
hello = "Woof!"
print_hello = True

if print_hello:
  print(hello)
```
````

And here's the rendered result:

```python
hello = "Woof!"
print_hello = True

if print_hello:
  print(hello)
```

The languages I use most are:

- `python`
- `json`
- `bash`
- `powershell`
