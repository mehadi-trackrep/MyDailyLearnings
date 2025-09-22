"""
LLM API calls are slow and can be expensive. If you send the same prompt to a model repeatedly, you're wasting time and money. A caching decorator elegantly solves this.

Problem: Redundant API calls for identical prompts.

Solution: A @cache decorator stores the result of a function call (e.g., an LLM completion for a specific prompt). If the same prompt is seen again, the decorator returns the stored result instead of making another API call.
"""

import functools

# A simple in-memory cache
llm_cache = {}

def cache(func):
    """A simple decorator to cache LLM calls."""
    @functools.wraps(func)
    def my_wrapper(prompt, model="gpt-4"):
        if (prompt, model) in llm_cache:
            print("--- Returning from CACHE ---")
            return llm_cache[(prompt, model)]
        else:
            print("--- Making a new API call ---")
            result = func(prompt, model)
            llm_cache[(prompt, model)] = result
            return result
    return my_wrapper

@cache
def get_llm_completion(prompt, model="gpt-4"):
    """Simulates a call to an LLM API."""
    print(f"Processing prompt for model: {model}...")
    return f"This is the AI's answer to '{prompt}'\n"

print(get_llm_completion("What is the capital of Bangladesh?"))
print(get_llm_completion("What is the capital of Bangladesh?"))
print(get_llm_completion("What is the capital of France?"))


"""
Output:

--- Making a new API call ---
Processing prompt for model: gpt-4...
This is the AI's answer to 'What is the capital of Bangladesh?'

--- Returning from CACHE ---
This is the AI's answer to 'What is the capital of Bangladesh?'

--- Making a new API call ---
Processing prompt for model: gpt-4...
This is the AI's answer to 'What is the capital of France?'

"""