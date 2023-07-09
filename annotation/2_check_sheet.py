"""
    * This document is a quick cheat sheet showing how to use type annotations for various common types in Python.
"""

# ---------------------------------------- 1. Variables ----------------------------------------
# Technically many of the type annotations show bellow are redundant, since mypy can usually infer the type of a variable from it's value.See inference and type annotations(https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html#type-inference-and-annotations) for more details.

# This is how you declare the type of a variable
from typing import Callable, Iterator, Optional, Union
from time import time
from typing import Optional
from typing import Union
from typing import List, Tuple, Dict, Set
age: int = 1

# You don't need to initialize a variable to annotate it
a: int  # OK (no value at runtime until assigned)

# Doing this can be useful in conditional branches
is_child: bool
if age < 18:
    is_child = True
else:
    is_child = False

# ---------------------------------------- 2. Built-in types ----------------------------------------
# For most types, just use the name of the type in the annotation
# Note that mypy can usually infer the type of the variable from it's value, so technically these annotations are redundant
x0: int = 0
x1: float = 0.1
x2: bool = True
x3: str = "hello"
x4: bytes = b"world"

# For collections on py3.9+, the type of collection item is in brackets
x5: list[int] = [1]
x6: set[float] = {.1, -3.14}

# For mappings, we need the types of both keys and values
x7: dict[str, int] = {"age": 18}    # py3.9+

# For tuples of fixed size, we specify the types of all the elements
x8: tuple[str, int, float] = ("", 1, .3)    # py3.9+

# For tuples of variable size, we use the type and ellipsis
x9: tuple[int, ...] = (1, 2, 3)     # py3.9+

# On python 3.8 and earlier, the name of the collection type is capitalized, and the type is imported from the "typing" module
x10: List[int] = [1]
x11: Tuple[int, ...] = (1, 2, 3)
x12: Tuple[str, int, float] = ("", 1, .12)
x13: Dict[str, int] = {"id": 123}
x14: Set[int] = {1}

# On python 3.10+, use the | operator when something could be one of a few types
x15: list[str | int | float] = [3.14, 2, "hello"]
# On earlier versions, use Union
x16: List[Union[str, int, float]] = [3.14, 2, "hello"]

# Use Optional[x] for a value that could be None
# Optional[x] is the same as x | None or Union[x, None]
x: Optional[str] = "something" if int(time()) % 2 == 0 else None
if x is not None:
    # Mypy understand x won't be None because of the if-statement
    print(x.upper())
# If you knew a value that can never be None due to some logic that mypy doesn't understand, use an assert
assert x is not None
print(x.upper())


# ---------------------------------------- 3. Functions ----------------------------------------
# This is how you annotate a function definition
def stringify(x: int) -> str:
    return str(x)


# And there's how you specify multiple arguments
def plus(x1: int, x2: int) -> int:
    return x1 + x2


# If a function not return a value, use None as the return type
# Default value for an argument goes after the type annotation
def show(value: str, excitement: int = 10) -> None:
    print(value + "!" * excitement)


# Note that arguments without a type is dynamically typed (treated as Any), and the function without any annotation not checked
def untyped(x):
    x.do_something() + 1 + "string"     # no errors




