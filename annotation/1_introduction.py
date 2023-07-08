"""
    * The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.

"""


# annotation example
def greeting(name: str) -> str:
    return 'Hello ' + name
