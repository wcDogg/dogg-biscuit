```
def json_via_importlib() -> dict[str, Any]:
  '''Get data from `nato.json` and return it as a dictionary.
  '''
  file_path = importlib.resources.files('morse_code').joinpath('nato.json')

  with file_path.open('r', encoding='utf-8') as file:
    data: dict[str, Any] = json.load(file)

  return data

def string_to_morse(string_to_convert: str) -> str:
  '''Converts a string to Morse code.
  '''
  data = json_via_importlib()
  characters: list = [char for char in string_to_convert]

  # Some conversion stuff, then ...
  print(morse)
  return(morse)

```
