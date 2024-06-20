Redis Cache Project
Overview

This project implements a caching mechanism using Redis for storing and retrieving data, along with additional functionalities like counting method calls, logging inputs and outputs, and replaying method call histories.
Features

    Caching: Data (strings, bytes, integers, floats) can be stored in Redis with a randomly generated key.

    Method Call Counting: Implemented using a decorator (@count_calls), it counts the number of times a method is called and increments a corresponding counter in Redis.

    Logging Inputs and Outputs: Another decorator (@call_history) logs inputs and outputs of method calls into Redis lists, allowing for historical analysis.

    Replay Functionality: The replay function retrieves and displays the history of calls for a particular method, showing inputs and outputs recorded in Redis.

Project Structure

    web.py: Contains functions to fetch HTML content from URLs and cache results using Redis.

    exercise.py: Implements the Cache class with decorators (count_calls and call_history) to add caching, counting, and logging capabilities.

Dependencies

    Python 3.7+
    Redis server
    redis Python library
    requests Python library

Installation

    Install Redis server from Redis.io.

    Install Python dependencies:

    pip install redis requests

Usage

    Basic Usage:

    python

    from exercise import Cache, replay

    cache = Cache()

    key = cache.store("example_data")
    print(cache.get(key))  # Retrieves stored data

    replay(cache.store)    # Displays method call history

    Detailed Functionality:
        store(data: Union[str, bytes, int, float]) -> str: Stores data in Redis and returns a unique key.
        get(key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]: Retrieves data from Redis, optionally converting it with a callable.
        get_str(key: str) -> Optional[str]: Retrieves data from Redis as a string.
        get_int(key: str) -> Optional[int]: Retrieves data from Redis as an integer.
        replay(method: Callable) -> None: Displays historical calls for a method.

Additional Notes

    Error Handling: Ensure Redis server is running and accessible. Handle decoding errors gracefully when retrieving data.

    Performance Considerations: Redis operations are optimized for speed, suitable for caching frequently accessed data.

Future Enhancements

    Expiration Policies: Implement flexible expiration times for cached data.

    Security: Enhance security with authentication and encryption mechanisms for sensitive data.

