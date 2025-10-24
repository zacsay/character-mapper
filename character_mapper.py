from argparse import ArgumentParser
from json import load
from pathlib import Path


def _normalise_map(map_: dict[str | int, str | int]) -> dict[str, str]:
    """Normalises the `map_` to use strs"""
    normalised: dict[str, str] = {}

    for k, v in map_.items():
        if isinstance(v, int):
            v = chr(v)

        if isinstance(k, int):
            normalised[chr(k)] = v
        else:
            normalised[k] = v

    return normalised


def map_string(map_: dict[str | int, str | int], string: str) -> str:
    """
    Maps the string according to `map_`.
    If `map_` contains ints, they are used as arguments to `chr`,
    otherwise they are used as the actual characters.
    """
    normalised = _normalise_map(map_)
    mapped: list[str] = []

    for c in string:
        if c in normalised:
            mapped.append(normalised[c])
        else:
            mapped.append(c)

    return "".join(mapped)


if __name__ == "__main__":
    parser = ArgumentParser(
        "Character Mapper", description="Map characters from one set to another"
    )

    parser.add_argument(
        "map", help="the path to the map to use", type=Path, default=None, nargs="?"
    )
    parser.add_argument("string", help="the string to map", default=None, nargs="?")

    parsed = parser.parse_args()

    map_ = parsed.map or Path(input("Enter the path to the map to use:\n> "))
    string = parsed.string or input("Enter the string to apply the mapping to:\n> ")

    map_ = load(map_.open())

    print(map_string(map_, string))
