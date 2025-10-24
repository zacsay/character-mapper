# Character Mapper
Map Unicode characters from one set to another.

## Installation and usage
1. Copy `character_mapper.py` somewhere useful
2. Invoke the script. The script has two optional positional arguments. If you do not provide one of them, you will be prompted when the script runs.
    - The first is the path to the mapping file to use
    - The second is the text to map

Please note: Character Mapper has only been tested with Python 3.14, however it should work with any reasonably modern version of Python.

## Mapping files
There are some character maps predefined in the `maps` directory.

If you want to make your own, create a JSON file with a single object mapping either characters or decimal code points to other characters or code points. 
Both can be used in the same file if this is more convenient.
