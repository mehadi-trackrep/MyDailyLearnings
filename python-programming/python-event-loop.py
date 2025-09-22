import asyncio
import random
import time

def blocking_image_processing(image_data):
    """A synchronous function that simulates a CPU-bound task."""
    print("Starting image processing...")
    # time.sleep(5)  # Simulate a 5-second processing time
    r = random.randrange(3, 6)
    time.sleep(r)  # Simulate variable processing time
    print("Finished image processing.")
    return f"processed_image.png - r: {r}"

async def handle_upload(image_data):
    """An async function that handles a request."""
    print("Received image upload.")
    # Offload the blocking task to another thread
    result = await asyncio.to_thread(blocking_image_processing, image_data)
    print(f"Image processed and saved as {result}")

async def main():
    # Simulate running two uploads at roughly the same time
    await asyncio.gather(
        handle_upload("image_one_data"),
        handle_upload("image_two_data")
    )

if __name__ == "__main__":
    asyncio.run(main())
