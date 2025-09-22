"""
For debugging and monitoring, you need to know exactly what prompts are being sent to the LLM and what raw responses are being received.

Problem: Manually adding logging statements to every AI function call is repetitive and clutters the code.

Solution: A @log_call decorator can automatically log the function's arguments (the prompt) and its return value (the LLM's response) to a file or monitoring service. This is invaluable for tracing the source of bad outputs or high token usage.

"""

import functools
import time
import random

def get_llm_completion(prompt: str, model: str = "gpt-4-turbo") -> str:
    """
    # Simulate LLM call
    This function simulates a network request to a Large Language Model API.
    - It prints status messages to the console.
    - It waits for 1-3 seconds to mimic network and processing latency.
    - It returns a templated string that includes the original prompt.
    """
    print(f"🤖 Calling model '{model}' with your prompt...")
    print("   (This is where a real API call to OpenAI, Google, etc. would happen)")
    
    # Simulate the time delay of a real API call
    processing_time = random.uniform(1.0, 3.0)
    time.sleep(processing_time)
    
    # In a real app, this response would come from the API
    response = (
        f"This is a simulated, high-quality response from model '{model}';\n"
        f"regarding your prompt: '{prompt[:40]}...'. The time is currently:\n"
        f"{time.strftime('%I:%M:%S %p')} in Bangladesh."
    )
    
    print(f"✅ Received response in {processing_time:.2f} seconds.")
    return response


def log_call(func):
    """A decorator to log function calls and results."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n==> LOG: Calling '{func.__name__}' with prompt: {args[0]}")
        result = func(*args, **kwargs)
        print(f"--> LOG: '{func.__name__}' returned: {result}")
        return result
    return wrapper

@log_call
@functools.cache # Decorators can be stacked!
def generate_summary(text):
    return get_llm_completion(text)

generate_summary("What are the best practices for fine-tuning a language model?")
generate_summary("What are the best practices for fine-tuning a language model?")

generate_summary("Python decorators are a powerful feature...")
generate_summary("What are the best practices for fine-tuning a language model?")

generate_summary("Python decorators are a powerful feature...")
generate_summary("Python decorators are a powerful feature...")