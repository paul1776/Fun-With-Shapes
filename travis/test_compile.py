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
  'name' : 'Compilation Test',
  'description' : 'Your source code compiles',
  'points_possible' : 20,
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
    print('Skipping due to an earlier error...')
    return ( test_case, skip_remaining_tests )
  else:
    test_case['test_ran'] = True
  
  from subprocess import Popen, PIPE, STDOUT
  import tempfile
  
  ## Compile given code
  
  print('Compiling given code...')
  
  givenFileList = [ 'ShapeHandler.java',
                    'Shape.java',
                    'ShapeDescription.java',
                    'ShapeException.java' ]
  
  for fileName in givenFileList:
    compile_output = tempfile.NamedTemporaryFile()
    print('Running "javac ' + fileName + '"...')
    test_timeout = False
    # $ javac <fileName>
    proc_compile = Popen( ["javac", fileName],
                          stdout=compile_output,
                          stderr=STDOUT,
                          text=True )
    
    try:
      proc_compile.wait( timeout=60 ) # Seconds
    except TimeoutError:
      proc_compile.kill()
      test_timeout = True
    
    # timeout error
    if ( test_timeout ):
      print('Timeout error: javac took longer than 60 seconds to complete.')
      print('Did you modify ' + fileName + ' in any way?')
      test_case['feedback'] = 'Test timed out; took longer than 60 seconds to compile ' + fileName
      skip_remaining_tests = True
      break # don't test remaining files
    # test returned
    else:
      proc_compile.poll()
      # compiler error
      if ( proc_compile.returncode != 0 ):
        print('Compilation error: javac return code non-zero')
        print('Compiler output:')
        print('-' * 10)
        with open( compile_output.name, 'r') as f:
          for line in f:
            print(line.rstrip())
        print('-' * 10)
        print('Review the javac output above to diagnose compiler error')
        print('You should restore all given code to its initial state in your repository and recommit.')
        test_case['feedback'] = 'Compiler error on "' + fileName + '"'
        skip_remaining_tests = True
        break # don't test remaining files
    # end else
  # end for
  
  # if given code did not compile, bail out
  if ( skip_remaining_tests ):
    print('All following tests will fail without properly-compiled given code; skipping remaining tests...')
    return ( test_case, skip_remaining_tests )
  else:
    print('All given code compiled.')
    print('')
  
  print('Compiling required code...')
  
  reqFileList = [   'Circle.java',
                    'Square.java',
                    'Rectangle.java',
                    'Triangle.java',
                    'FunWithShapes.java' ]
  
  for fileName in reqFileList:
    compile_output = tempfile.NamedTemporaryFile()
    print('Running "javac ' + fileName + '"...')
    test_timeout = False
    # $ javac <fileName>
    proc_compile = Popen( ["javac", fileName],
                          stdout=compile_output,
                          stderr=STDOUT,
                          text=True )
    
    try:
      proc_compile.wait( timeout=60 ) # Seconds
    except TimeoutError:
      proc_compile.kill()
      test_timeout = True
    
    # timeout error
    if ( test_timeout ):
      print('Timeout error: javac took longer than 60 seconds to complete.')
      test_case['feedback'] = 'Test timed out; took longer than 60 seconds to compile ' + fileName
      skip_remaining_tests = True
      break # don't test remaining files
    # test returned
    else:
      proc_compile.poll()
      # compiler error
      if ( proc_compile.returncode != 0 ):
        print('Compilation error: javac return code non-zero')
        print('Compiler output:')
        print('-' * 10)
        with open(compile_output.name, 'r') as f:
          for line in f:
            print(line.rstrip())
        print('-' * 10)
        print('Review the javac output above to diagnose compiler error')
        test_case['feedback'] = 'Compiler error on "' + fileName + '"'
        skip_remaining_tests = True
        break # don't test remaining files
    # end else
  # end for
  
  # Print a skip notification
  if ( skip_remaining_tests ):
    print('All code must compile to continue; skipping remaining tests...')
  else:
    print('All required code compiled')
    test_case['points_earned'] = test_case['points_possible']
    test_case['test_passed'] = True
    # Compile the test code right here
    import test_shapes_setup
    
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