# COS 397 Exercise

This is a skeleton repository for your exercise. 
The goal of this exercise is to implement a Python package for sorting integer 
lists using the DevOps software development approach.

**Warning**: If working on windows, some directories and files in this archive
will not be visible because they start with a '.'. In the file browser, change 
the View to display "Hidden items".

You will need to:
1. Implement the algorithms for bubble, quick and insertion sort, see sort_lib directory,
code should be documented using standard Python practices (there are several [docstring 
styles](https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format)
select one and be consistent).
2. Implement testing using the [pytest](https://docs.pytest.org/en/6.2.x/) framework, see test directory.
3. Implement linting, style checking using both [flake8](https://flake8.pycqa.org/en/latest/) and 
[black](https://black.readthedocs.io/en/stable/). 
4. Modify the GitHub actions workflow so that it tests and builds the package for all 
three operating systems (OSX/Linux/Win) and for Python versions 3.6 and 3.9.
5. Modify this file to describe this repository and the DevOps workflow you 
implemented (add badges to this file showing testing status).

Possible work division, three sub-teams:
1. Implementing algorithm code and documentation (tasks 1,5).
2. Implementing testing code, mastering pytest, black, flake8 (tasks 2,3,5).
3. Understanding pytest, black, flake8 and mastering GitHub workflows (tasks 4,5).

