import json
from typing import Optional, Callable, List


def parse_json(json_str: str, required_fields: Optional[List[str]] = None,
               keywords: Optional[List[str]] = None, keyword_callback: Optional[Callable] = None) -> dict:
    """Applies keyword_callback() to keywords which are in required_fields"""

    json_doc = json.loads(json_str)
    for key in json_doc:
        if key in required_fields:
            splitted_value = json_doc[key].split()
            for word in splitted_value:
                if word in keywords:
                    word = keyword_callback(word)

    return json_doc
