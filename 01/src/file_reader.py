from typing import Union, TextIO, List

def _make_set(lst: List[str]):
    if len(lst) == 1:
        return set([lst[0]])
    else:
        return set(lst)

def file_reader(file: Union[str, TextIO], words: List[str]) -> List[str]:
    if type(file) == str:
        stream = open(file, encoding='utf-8')
    elif type(file) == TextIO:
        stream = file

    for string in stream:
        if string[-2:] == "\n":
            string = string[:-2]

        set1 = _make_set([word.lower() for word in string.split()])
        set2 = _make_set([word.lower() for word in words])
        if set1.intersection(set2):
            yield string.rstrip('\n')

    stream.close()
