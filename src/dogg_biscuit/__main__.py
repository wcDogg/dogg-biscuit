"""Command-line interface."""
import inspect

import click


ASCII = """
                             __
      ,                    ," e`--o
     ((                   (  | __,'
      \\\\~----------------' \\_;/
@ ! > (                      /
      /) ._______________.  )
     (( (               (( (
      ``-'               ``-'
"""


@click.command()
@click.version_option()
def main() -> None:
    """A tech writer's first Hypermodern Python Cookiecutter project."""
    print(inspect.cleandoc(ASCII))


if __name__ == "__main__":
    main(prog_name="dogg-biscuit")  # pragma: no cover
