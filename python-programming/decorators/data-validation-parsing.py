import json
import functools
from pydantic import BaseModel, ValidationError

class UserProfile(BaseModel):
    name: str
    age: int

def ensure_json_output(model):
    """Decorator to parse and validate LLM output against a Pydantic model."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            raw_output = func(*args, **kwargs)
            print(f"Raw LLM output: {raw_output}")
            try:
                data = json.loads(raw_output)
                return model(**data)
            except (json.JSONDecodeError, ValidationError) as e:
                print(f"Validation Error: {e}. Output was: {raw_output}")
                raise ValueError("LLM output failed validation.")
        return wrapper
    return decorator

@ensure_json_output(model=UserProfile)
def extract_user_profile(text: str):
    """Simulates an LLM extracting a user profile into JSON."""
    # This output is valid JSON
    return '{"name": "Alice", "age": 30}'

    # This output is INVALID (e.g., a common LLM mistake)
    return "{'name': 'Bob', 'age': 25}" # Uses single quotes, not valid JSON

try:
    user = extract_user_profile("Some text about Bob who is 25 years old.")
    print(user)
except ValueError as e:
    print(e)