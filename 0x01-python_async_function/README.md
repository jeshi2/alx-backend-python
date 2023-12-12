# Python - Async

## Requirements
- Python 3.7
- Tested on Ubuntu 18.04 LTS
- Editors: vi, vim, emacs
- Coding style: pycodestyle (version 2.5.x)

## Overview
This project demonstrates the usage of asynchronous coroutines and tasks in Python. It includes several modules for working with random delays and asyncio features.

## Modules

### 0-basic_async_syntax.py
- Contains the basic asynchronous coroutine `wait_random` that waits for a random delay.

### 1-concurrent_coroutines.py
- Implements the `wait_n` async routine that spawns `wait_random` n times with a specified max_delay.

### 2-measure_runtime.py
- Provides the `measure_time` function to measure the total execution time for `wait_n(n, max_delay)` and returns `total_time / n`.

### 3-tasks.py
- Introduces the `task_wait_random` function, creating an asyncio.Task using the `wait_random` coroutine.

### 4-tasks.py
- Extends the functionality to create an asyncio.Task list using the `task_wait_random` coroutine with `task_wait_n` function.

## Usage
Each module contains example usage at the end of the file. You can run these examples to see the functionality in action.

### Example:
```bash
$ python3 1-concurrent_coroutines.py
$ python3 2-measure_runtime.py
$ python3 3-tasks.py
$ python3 4-tasks.py
```


## Author
Antony Wagwnaa

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.