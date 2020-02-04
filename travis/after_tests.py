# **********
# after_tests.py
# 
# Common "last" script for all assignments
#
# **********
import library

results = library.run_after_test_suite()

if ( results == 0 ):
  exit(0)
else:
  exit(1)