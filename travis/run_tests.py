# **********
# run_tests.py
#
# Wrapper to execute all test cases
#
# **********

# Shared test resources

# Run test suite start-up
import before_tests

# Run each test case
# *****

import test_commit
import test_files
import test_compile # test_shapes_setup inside to compile ShapeTester.java
import test_circle
import test_square
import test_rectangle
import test_triangle
import test_output

# *****
# Run test suite ending (print rubric)
import after_tests
