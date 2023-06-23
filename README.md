# ToyotaCar Logger Example

## Summary of Skills and Concepts

* Use of Python's logging module
* Creation and configuration of loggers in Python
* Creation and utilization of Python classes (ToyotaCar class)
* Python file handling and manipulation

## Introduction

This repository contains a Python code example that showcases the creation and usage of a logger using the Python logging module. The focus of this example is the implementation of logging within the context of a ToyotaCar class.

## Usage

To run the code and see the logger in action:

1. Ensure you have Python installed on your system.
2. Clone this repository or download the code files.
3. Open a terminal or command prompt and navigate to the directory where the code files are located.
4. Execute the following command to run the code:

```bash
python main.py
```

This will execute the code and demonstrate the logging functionality.

## Description

The code defines a ToyotaCar class that represents a Toyota car. It demonstrates how to initialize a logger, set its level, define a formatter, and add a file handler. The logger is used to log information about the creation of a ToyotaCar instance.

The ToyotaCar class includes various methods to interact with the car, such as starting and stopping the engine, accelerating, braking, and displaying car information.

## Logging Details

* The logger is initialized using `logging.getLogger(__name__)`, where `__name__` represents the module name.
* The logger's level is set to `logging.INFO`, which means it will capture log messages with an informational level or above.
* The logger uses a `Formatter` object with the format `'%(levelname)s:%(name)s:%(message)s'`, which specifies how the log messages should be formatted.
* A `FileHandler` is added to the logger, which directs the log messages to a file named `toyotas.log`.
* When a new `ToyotaCar` instance is created, an informational log message is recorded using the `logger.info()` method.

The code also demonstrates the usage of the `ToyotaCar` class by creating an instance, displaying its information, starting the engine, accelerating, braking, and stopping the engine.

Feel free to explore the code and experiment with different logging configurations to further understand the logging functionality in Python.

## Note

Remember to configure the logger as per your application's requirements and modify the code accordingly.

## Requirements

* Python 3.x
* logging module (included in the Python standard library)

## Logger Diagram

*Insert Logger Diagram Here*
