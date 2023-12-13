# Python - Async Comprehension

This repository showcases a series of asynchronous Python scripts, designed to illustrate fundamental concepts in asynchronous programming using the asyncio library.

## Task 0: Asynchronous Generator

The script `0-async_generator.py` introduces an asynchronous generator. It yields random numbers after a 1-second asynchronous pause in each iteration.

**Usage:**
```bash
$ ./0-main.py
```

## Task 1: Async Comprehension

In `1-async_comprehension.py`, the asynchronous generator from Task 0 is employed to collect 10 random numbers using async comprehensions.

**Usage:**
```bash
$ ./1-main.py
```

## Task 2: Measure Runtime

The `2-measure_runtime.py` script measures the total runtime of executing the async_comprehension coroutine four times in parallel using asyncio.gather.

**Usage:**
```bash
$ ./2-main.py
```

**Prerequisites:**
- Python 3.7 or later.

## Getting Started

1. Clone the repository:
   ```bash
   $ git clone https://github.com/your_username/async-python-tasks.git
   $ cd async-python-tasks
   ```

2. Grant execution permissions to the Python scripts:
   ```bash
   $ chmod +x *.py
   ```

3. Run the desired task script:
   ```bash
   $ ./script_name.py
   ```

## Additional Notes

Feel free to explore and modify the code for educational purposes. We encourage you to delve into the scripts to gain insights into asynchronous programming with Python.

For detailed information on each task, refer to the respective script files.

---

**Author:** Antony Wagwana
