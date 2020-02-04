# *****
# Test case template:
# 1. Define test_case object
# 2. Define do_test( test_data, test_case, skip_remaining_tests )
# 3. Call ( test_data, skip_remaining) = library.run_before_test( test_case )
# 4. Perform test
# 5. Calll library.run_after_test( test_case, skip_remaining_tests )

import library

# *****
# 1. Define test_case object
# - Required fields:
# - - name
# - - description
# - - points_possible
# - - points_earned (initialize to zero)
# - - test_ran (initialize to False)
# - - test_passed (initialize to False)
# *****

test_case = {
  'name' : 'File Submission Test',
  'description' : 'Your commit contains all the required files with correct names.',
  'points_possible' : 10,
  'points_earned' : 0,
  'test_ran' : False,
  'test_passed' : False,
  'feedback' : '',
}

# *****
# 2. Define do_test
# Inputs:
# - test_case : Defined above; update fields within do_test
# - skip_remaining_tests : Update within do_test
# Outputs:
# - test_case : Updated test case data
# - skip_remaining_tests : Updated skip flag
# *****

def do_test( test_case, skip_remaining_tests ):
  
  # Short-circuit if skipping
  if ( skip_remaining_tests ):
    return ( test_case, skip_remaining_tests )
  else:
    test_case['test_ran'] = True
  
  from subprocess import Popen, PIPE, STDOUT
  
  ## Check that given code is still present
  
  print('Verifying that all given code is still present in your repository...')
  
  givenFileList = [ 'ShapeHandler.java',
                    'Shape.java',
                    'ShapeDescription.java',
                    'ShapeException.java' ]
  
  for fileName in givenFileList:
    print('Looking for "' + fileName + '" within your repository...')
    test_timeout = False
    # $ test -e <fileName>
    proc_exists = Popen( ["test", "-e", fileName ] )
    
    try:
      proc_exists.wait( timeout=60 ) # Seconds
    except TimeoutError:
      proc_exits.kill()
      test_timeout = True
    
    # Timeout failure
    if ( test_timeout ):
      print('Timeout error: test took longer than 60 seconds to complete')
      print('Do you have a LOT of files in your repository?')
      print('')
      test_case['feedback'] = 'Test timed out; took longer than 60 seconds to find ' + fileName
      skip_remaining_tests = True
      break # don't test remaining files
    # test returned
    else:
      proc_exists.poll()
      # No file
      if ( proc_exists.returncode != 0 ):
        print('No file named "' + fileName + '" exists in your repository.')
        print('You should restore all given code to its initial state in your repository and recommit.')
        test_case['feedback'] = 'Given file "' + fileName + '" not found in your repository'
        skip_remaining_tests = True
        break # don't test remaining files
      # File exists
      else:
        print('A file named "' + fileName + '" was found in your repository.')  
    # end else
  # end for  
  
  # if given code is missing, bail out
  if ( skip_remaining_tests ):
    print('All following tests will fail without given code present; skipping remaining tests...')
    return ( test_case, skip_remaining_tests )
  else:
    print('All given code is present!')
    print('')
  
  ## Check that required files are present
  
  print('Verifying that all required files are present in your repository...')
  
  reqFileList = [   'ClassDiagram.pdf',
                    'Circle.java',
                    'Square.java',
                    'Rectangle.java',
                    'Triangle.java',
                    'FunWithShapes.java' ]
  
  for fileName in reqFileList:
    print('Looking for "' + fileName + '" within your repository...')
    test_timeout = False
    # $ test -e <fileName>
    proc_exists = Popen( ["test", "-e", fileName ] )
    
    try:
      proc_exists.wait( timeout=60 ) # Seconds
    except TimeoutError:
      proc_exits.kill()
      test_timeout = True
    
    # Timeout failure
    if ( test_timeout ):
      print('Timeout error: test took longer than 60 seconds to complete')
      print('Do you have a LOT of files in your repository?')
      print('')
      test_case['feedback'] = 'Test timed out; took longer than 60 seconds to find ' + fileName
      skip_remaining_tests = True
      break # don't test remaining files
    # test returned
    else:
      proc_exists.poll()
      # No file
      if ( proc_exists.returncode != 0 ):
        print('No file named "' + fileName + '" exists in your repository.')
        print('Check that:')
        print(' - The file was added to git tracking and committed')
        print(' - The file is in your repository root directory (and not, e.g., ./src/' + fileName)
        print(' - The file has the exact name "' + fileName + '"')
        test_case['feedback'] = 'File "' + fileName + '" not found in your repository'
        skip_remaining_tests = True
        break # don't test remaining files
      # File exists
      else:
        print('A file named "' + fileName + '" was found in your repository.')
    
    # Print a skip notification
  if ( skip_remaining_tests ):
    print('All following tests will fail without required files present; skipping remaining tests...')
  else:
    print('All required files are present!')
    test_case['points_earned'] = test_case['points_possible']
    test_case['test_passed'] = True
    
  return test_case, skip_remaining_tests       

# *****
# 3. Call run_before_test
# *****
( test_data, skip_remaining_tests ) = library.run_before_test( test_case )

# *****
# 4. Perform test
# *****

(test_case, skip_remaining_tests) = do_test( test_case, skip_remaining_tests )

# *****
# 5. Call run_after_test
# *****
library.run_after_test( test_data, test_case, skip_remaining_tests )