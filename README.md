![Python](https://www.python.org/static/community_logos/python-logo-generic.svg)

# Python Multi-threading

Python multi-threading tests and examples.

## Installation

```sh
pip install -r requirements.txt
```

## How to Run

To run the functions:

```sh
python3 -m python_multithreading.main_module
python3 -m python_multithreading.multithreading_standard
python3 -m python_multithreading.multithreading_io
python3 -m multithreading_worker
python3 -m multithreading_worker_counter
```
![running.png](resources/running.png)
![threadPool_worker.png](resources/threadPool_worker.png)

To run all the tests in directory 'tests':

```sh
python -m unittest discover -s tests
```
![tests.png](resources/tests.png)

## Examples

* [main_module.py](python_multithreading/main_module.py): The basic thread test.
* [multithreading_standard.py](python_multithreading/multithreading_basic.py): It runs many standard threads.
* [multithreading_io.py](python_multithreading/multithreading_io.py): It performs I/O operations, reading files in a multi-threading context.
* [multithreading_worker.py](python_multithreading/multithreading_worker.py): It implements a basic ThreadPool with Workers.
* [multithreading_worker_counter.py](python_multithreading/multithreading_worker_counter.py): A counter ThreadPool with Workers synchronizing and locking.

## Author

* Wallace Espindola, Sr. Software Engineer / Java & Python Dev
* E-mail: wallace.espindola@gmail.com
* LinkedIn: https://www.linkedin.com/in/wallaceespindola/
* Website: https://wtechitsolutions.com/

## License

* This project is released under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
* Copyright © 2024 [Wallace Espindola](https://github.com/wallaceespindola/).