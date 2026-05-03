# Introduction

This document is to show my growth mindset process in any programming language I've learned, including Python Fundamentals for this repository.  Eventhough the documentation is not neat and ad hoc due to intense learning process juggling between learning other programming language, reading novels of Manual Docs, and doing some real projects, so I documented my learning here as I possibly could.

### Learning 1: Pengecekan Style Guide PEP8
**Branch: 10_1_pep8StyleGuide**<br>
In this learning process, I've been introduced with 3 lints, which are pycodestyle, pylint, and flake8.  In this learning process, I've been asked to install 3 of them:
1. Pycodestyle _(before was PEP8)_
```
pip install pycodestyle
```
2. Pylint
```
pip install pylint
```
3. Flake8
```
pip install flake8
```
<br>
After I've install 3 Lint above, I've been instructed to create a new python file called calculator.py, with code below:
```
class Kalkulator:
    """kalkulator tambah kurang"""
    def __init__(self, _i):
        self.i = _i
    def tambah(self, _i): return self.i + _i
    def kurang(self, _i):
    return self.i - _i
```

**Note:** I Accidentally keep the 'return' statement without indentation, to show how this work.<br>

I then run the code above using each lint like above after done installing them:
1. Pycodestyle
    ```
    pycodestyle calculator.py
    ```
    The Output:<br>
    ![Alt text](readme_image/10_1_pep8StyleGuide/pycodestyle_lint_error.png)

2. Pylint
    ```
    pylint calculator.py
    ```
    The Output:<br>
    ![Alt text](readme_image/10_1_pep8StyleGuide/pylint_lint_error.png)

3. Flake8
    ```
    flake8 calculator.py
    ```
    The Output:<br>
    ![Alt text](readme_image/10_1_pep8StyleGuide/flake8_lint_error.png)

From each results above, it does show different error notifications between each lints used.  The errors specified are all the same, which shows indentation error in line 7.<br>
<br>

**The Correct Version of calculator.py Code**<br>
Here's the corrected version of calculator.py after adjust the line 7 with the correct indentation:
```
class kalkulator:
    """kalkulator tambah kurang"""
    def __init__(self, _i):
        self.i = _i
    def tambah(self, _i): return self.i + _i
    def kurang(self, _i):
        return self.i - _i
```
The result of each Lints:
1. Pycodestyle
    ```
    pycodestyle calculator.py
    ```
    The Output: No Errors
2. Flake8
    ```
    flake8 calculator.py
    ```
    The Output: No Errors
3. Pylint
    ```
    pylint calculator.py
    ```
    Result: Shows a docs error<br>
    ![Alt text](readme_image/10_1_pep8StyleGuide/pylint_lint.png)
<br>
For Point no 1 and 2, when we run the pycodestyle and flake8, it returns no error:<br>
![Alt text](readme_image/10_1_pep8StyleGuide/flake8_pycodestyle_lint.png)
<br>
But on Point no 3 when we run the Pylint, it returns the docs error due to because Pylint requires the developers to specify docstrings documentations between each functions (def in python).  But that's actually fine, does not shows the real technical errors in our programs, just to makesure that our code becomes more perfect in the future.