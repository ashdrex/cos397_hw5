# COS 397 Exercise

This repository contains three sorting algorithms, a suite of tests, and a continuous integration workflow. Each algorithm takes an list of integers as an argument, and returns a sorted version of that list. All algorithms can be found in sort_lib/int_sort.py.

Our continuous integration framework has three primary steps. First, we lint with both black and flake8, ensuring consistent styling. We then test that each algorithm is produces a list in ascending order when tested on a list of random integers. If both of these stages are passed, we package the program. All tests can be found in test/test_int_sort.py.
