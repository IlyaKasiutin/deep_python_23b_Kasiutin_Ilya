from typing import Union, List
import _io


def file_reader(file: Union[str, _io.TextIOWrapper], words: List[str]) -> List[str]:
    """Finds strings containing at least one word from words list"""

    stream = None
    if isinstance(file, str):
        stream = open(file, encoding='utf-8')
    elif isinstance(file, _io.TextIOWrapper):
        stream = file

    for string in stream:
        if string[-2:] == "\n":
            string = string[:-2]

        lower_string = set(map(lambda x: x.lower(), string.split()))
        lower_words = list(map(lambda x: x.lower(), words))

        if lower_string.intersection(lower_words):
            yield string.rstrip('\n')

    if isinstance(file, str):
        stream.close()
