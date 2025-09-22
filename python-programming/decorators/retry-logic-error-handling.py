"""
API calls to GenAI services can fail due to network issues, rate limits, or server-side errors. A decorator can automatically handle retries.

Problem: Transient errors from LLM APIs can crash your application flow.

Solution: A @retry decorator wraps the API call in a try/except block. If a specific error occurs (like a 503 Service Unavailable), it waits for a short period and tries again, up to a specified number of attempts.
"""
import time
import functools

def retry(attempts=3, delay=2):
    """A decorator for retrying a function on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Retrying up to {attempts} times with {delay}s delay...")
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i+1}/{attempts} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            raise Exception("All retry attempts failed")
        return wrapper
    return decorator

@retry(attempts=3, delay=1)
def fetch_data_from_flaky_api():
    """Simulates a call to an unreliable API."""
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("API service is unavailable")
    return "Successfully fetched data!"

# This will likely fail a few times before succeeding
print(fetch_data_from_flaky_api())