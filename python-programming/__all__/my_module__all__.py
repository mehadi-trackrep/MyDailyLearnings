"""
The __all__ variable is used to define the public interface of a module.
It is a list of strings that specifies which names should be imported when a user imports the module using from module import *.
"""

def public_function():
    print("This is a public function.")

def _private_function(): # protected for internal use but exposeable via __all__
    print("This is a private function.")
    
def _private_function_v2(): # protected for internal use but exposeable via __all__
    print("This is a private function v2.")

class PublicClass:
    def __init__(self):
        print("PublicClass instance created.")

__all__ = ["public_function", "PublicClass", "_private_function"]  # Explicitly include _private_function