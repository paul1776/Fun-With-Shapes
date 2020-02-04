# **********
# library.py
#
# Helper functions to support autograde test writing
#
# ***********
import json

test_data_filename = 'test_data.json'
json_indent = 2

# *****
# run_before_tests
# - Called from before_tests.py
# - Prints test suite header and initializes test data json
# *****

def run_before_test_suite( assignment_info ):
  print_test_suite_header( assignment_info )
  create_test_suite_data( assignment_info )

def print_test_suite_header( assignment_info ):
  # Test suite header output:
  ##
  ## ******************************
  ## Autograder Script
  ## COSC 150 : Advanced Programmming
  ## Assignment <number> : <name>
  ##
  ## ******************************
  ##
  
  name = assignment_info['name']
  number = assignment_info['number']
  
  print('')
  print('*' * 30)
  print('Autograder Script')
  print('COSC 150 : Advanced Programming')
  print('Assignment', number, ':', name)
  print('')
  print('*' * 30)
  print('')
  
  return

def create_test_suite_data( assignment_info ):
  test_data = {
    'assignment_info' : assignment_info,
    'test_count' : 0,
    'test_cases' : [],
    'tests_run' : 0,
    'tests_passed' : 0,
    'all_tests_passed' : True,
    'skip_remaining_tests' : False,
    'tests_skipped' : 0,
  }
  with open( test_data_filename, 'w' ) as outfile:
    json.dump( test_data, outfile, indent=json_indent )
  
  return

# *****
# run_after_tests
# - Called from after_tests.py
# - Prints results of test cases, returns overall pass/fail
# *****

def run_after_test_suite():
  with open( test_data_filename, 'r' ) as infile:
    test_data = json.load( infile )
  
  print_test_suite_results( test_data )
  print_test_suite_rubric( test_data )
  
  if ( test_data['all_tests_passed'] ):
    return 0
  else:
    return 1

def print_test_suite_results( test_data ):
  # Test suite result output:
  ##
  ## ******************************
  ## TEST RESULTS:
  ## Total tests:
  ## Tests run:
  ## Tests passed:
  ## Tests skipped:
  ##
  ## You successfully passed all tests!
  ## One or more tests were failed/skipped
  ## ******************************
  
  test_count = test_data['test_count']
  tests_run = test_data['tests_run']
  tests_passed = test_data['tests_passed']
  tests_skipped = test_data['tests_skipped']
  all_tests_passed = test_data['all_tests_passed']
  
  print('')
  print('*' * 30 )
  print('TEST RESULTS')
  print('Total tests:', test_count)
  print('Tests run:', tests_run)
  print('Tests passed:', tests_passed)
  print('Tests skipped:', tests_skipped)
  print('')
  if ( all_tests_passed ):
    print('You successfully passed all tests!')
  else:
    print('One or more tests were failed/skipped!')
  print('*' * 30)
  print('')
  
  return

def print_test_suite_rubric( test_data ):
  test_cases = test_data['test_cases']
  
  # Rubric header row
  print( '-' * 30 )
  print( '| Ran | Pass | Pts / Tot | Description' )
  print( '-' * 30 )
  
  total_points_earned = 0
  total_points_possible = 0
  
  for case in test_cases:
    ## | (X) | # / # | <Description>
    print( '| [{}] |  [{}] | {:>3} / {:3} | {}'.format(
       'X' if case['test_ran'] else ' ',
       'X' if case['test_passed'] else ' ',
       case['points_earned'],
       case['points_possible'],
       case['description']
       ) # End format()
    ) # End print()
    print( '-' * 30 )
    
    total_points_earned += case['points_earned']
    total_points_possible += case['points_possible']
  
  # End for
  
  # Print total score row
  print ( ' ' * 13, ' {:>3} / {:>3} | Total Autograder points'.format(
      total_points_earned,
      total_points_possible
      ) # End format()
  ) # End print()
  print('')
  
  return

# *****
# read_test_data
# - Fetch from json and provide to test case
# - Print test case header
# *****

def run_before_test( test_case ):
  
  test_data = load_test_data( test_case )
  
  test_number = test_data['test_count']
  print_test_header( test_case, test_number )
  
  skip_remaining_tests = test_data['skip_remaining_tests']
  
  return (test_data, skip_remaining_tests)

def load_test_data( test_case ):
  with open( test_data_filename, 'r' ) as infile:
    test_data = json.load(infile)
  
  # Append current test to test_data
  test_data['test_count'] += 1
  test_data['test_cases'].append( test_case )
  
  return test_data

def print_test_header( test_case, test_number ):
  # Test header output:
  ## 
  ## ********************
  ## TEST <test_number> : <test_name>
  ##
  ## <test_description>
  ## --------------------
  ##
  
  print('')
  print('*' * 20)
  print('TEST', test_number, ':', test_case['name'])
  print('')
  print(test_case['description'])
  print('-' * 20)
  print('')
  
  return

# *****
# - Print test results
# - Update test_data and dump
# *****

def run_after_test( test_data, test_case, skip_remaining_tests ):
  print_test_results( test_case, skip_remaining_tests )
  
  # Update summary statistics in test_data
  if ( test_case['test_ran'] ):
    test_data['tests_run'] += 1
  else:
    test_data['tests_skipped'] += 1
  
  if ( test_case['test_passed'] ):
    test_data['tests_passed'] += 1
    
  test_data['all_tests_passed'] = test_data['all_tests_passed'] and test_case['test_passed']
  
  test_data['skip_remaining_tests'] = skip_remaining_tests
  
  # Write to json
  with open( test_data_filename, 'w') as outfile:
    json.dump( test_data, outfile, indent=json_indent)
  
  return

def print_test_results( test_case, skip_remaining_tests ):
  # Test results output:
  ##
  ## --------------------
  ## TEST RESULT: <pass/fail/skip>
  ## Points earned: <points_earned>/<points_possible>
  ## Feedback:
  ## <feedback>
  ##
  ## <skip message>
  ## ********************
  
  if ( test_case['test_ran'] ):
    if ( test_case['test_passed'] ):
      test_result = "PASS"
    else:
      test_result = "FAIL"
  else:
    test_result = "SKIP"
  
  print('')
  print('-' * 20)
  print('TEST RESULT:', test_result)
  print('Points earned: {:>3} / {:>3}'.format(
      test_case['points_earned'],
      test_case['points_possible']
      ) # end format()
  ) # end print()
  print('Feedback:')
  print(test_case['feedback'])
  print('')
  if ( skip_remaining_tests ):
    print('Due to prior failure, remaining tests will be skipped')
  print('*' * 20)
  
  return

  
  