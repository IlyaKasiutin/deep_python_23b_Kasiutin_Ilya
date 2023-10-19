"""CustomMeta definition"""

from typing import Dict, Any


class CustomMeta(type):
    """Metaclass which adds 'custom_' to each method
    and attribute name of inherited classes"""

    def __new__(mcs, name, bases, classdict: Dict[str, Any], **kwargs):
        for param in classdict.copy():
            if not (param.startswith("__") and param.endswith("__")):
                classdict["custom_" + param] = classdict.pop(param)
        cls = super().__new__(mcs, name, bases, classdict, **kwargs)
        cls.__setattr__ = CustomMeta.custom_setattr

        return cls

    def custom_setattr(cls, key, val):
        """Overrides __setattr__ of child classes.
        Needed for changing dynamic attributes"""

        if not (key.startswith("__") and key.endswith("__")):
            key = "custom_" + key

        object.__setattr__(cls, key, val)
