"""
    * This document is a quick cheat sheet showing how to use type annotations for various common types in Python.
"""

# ---------------------------------------- Variables ----------------------------------------
# Technically many of the type annotations show bellow are redundant, since mypy can usually infer the type of a variable from it's value.See inference and type annotations(https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html#type-inference-and-annotations) for more details.

# This is how you declare the type of a variable
age: int = 1

# You don't need to initialize a variable to annotate it
a: int  # OK (no value at runtime until assigned)

# Doing this can be useful in conditional branches
is_child: bool
if age < 18:
    is_child = True
else:
    is_child = False
