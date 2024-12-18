# About Python

- Python is a powerful and versatile general-purpose programming language known for its readability, ease of use, and extensive libraries.
- Why Python?
  - Beginner-Friendly: Python's syntax is clear and concise, resembling natural language, making it easier to learn and write compared to languages with complex syntax.
  - Versatile: Python can be used for various tasks, including web development, data science, machine learning, scripting, automation, and more.
  - Large Community and Libraries: Python boasts a vast and active community that contributes to a rich ecosystem of libraries and frameworks, providing ready-made solutions for many common programming needs.
- Key Features
  - Dynamic Typing: Python doesn't require you to explicitly declare data types for variables. The type is inferred based on the assigned value, offering flexibility.
  - Object-Oriented Programming (OOP): Python supports OOP principles, allowing you to structure your code using classes and objects. While not as strictly typed as languages like Java, OOP in Python can help organize complex code.
  - Interpreted Language: Python code is interpreted line by line by the Python interpreter at runtime, making development faster and more interactive compared to compiled languages.

## installation and setup - windows only

- download one of the latest python version from this [download_page](https://www.python.org/downloads/windows/) and follow the installation instructions mentioned [here](https://docs.python.org/3/using/windows.html#the-full-installer)
- for other platforms check this link [downloads](https://www.python.org/downloads/)
- execute below command in windows command prompt to check whether python installation is successful. if installation is successful then python version is displayed once command executed.

```bash
python -V
```

- Python virtual environment
  - execute `python -m venv .venv` command in command prompt to create virtual environment in the current directory with `.venv` name.
  - change `.venv` to the path of your choice if you wish to do so.
  - after virtual environment creation you need to activate virtual environment to execute scripts in virtual environment.
  - using command prompt call this file `.venv\Scripts\activate` to activate virtual environment.
  - execute `python -m pip install pip ---upgrade` to upgrade `pip` to latest available version.
