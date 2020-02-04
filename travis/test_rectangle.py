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
  'name' : 'Rectangle Class Test',
  'description' : 'Your Rectangle class instantiates; correcly computes area; and correctly computes perimeter.',
  'points_possible' : 15,
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
  
  keep_going = True
  
  from subprocess import Popen, PIPE, STDOUT
  import tempfile
  
  ## Instantiate test
  print('Attempting to instantiate a Rectangle...')
  
  instance_output = tempfile.NamedTemporaryFile()
  
  test_timeout = False
  # $ java TestShapes rectangle-instantiate
  proc_instantiate = Popen( ['java', 'TestShapes', 'rectangle-instantiate'],
                            stdout=instance_output,
                            stderr=STDOUT,
                            text=True )
  try:
    proc_instantiate.wait( timeout=60 ) # Seconds
  except TimeoutError:
    proc_instantiate.kill()
    test_timeout = True
    
  # timeout error
  if ( test_timeout ):
    print('Timeout error: java took longer than 60 seconds to complete.')
    print('')
    test_case['feedback'] = 'Test timed out; took longer than 60 seconds to instantiate Rectangle'
  else:
    proc_instantiate.poll()
    # runtime error
    if ( proc_instantiate.returncode != 0 ):
      print('Run-time error: java return code non-zero')
      print('Program output:')
      print('-' * 10)
      with open(instance_output.name, 'r') as f:
        for line in f:
          print(line.rstrip())
      print('-' * 10)
      print('Review the java output above to diagnose error')
      print('')
      test_case['feedback'] = 'Error instantiating Rectangle'
      keep_going = False
    else:
      print('Instantiation successful')
      print('')
      test_case['points_earned'] += test_case['points_possible'] / 3

  # If instantiation fails, stop
  if ( not keep_going ):
    print('All following Rectangle tests will fail without properly-instantiated Rectangles; skipping the rest of this test...')
    return ( test_case, skip_remaining_tests )
  
  ## Area test
  print('Testing Rectangle.getArea()...')
  
  area_output = tempfile.NamedTemporaryFile()
  
  test_timeout = False
  # $ java TestShapes rectangle-area
  proc_area = Popen( ['java', 'TestShapes', 'rectangle-area'],
                     stdout=area_output,
                     stderr=STDOUT,
                     text=True )
  try:
    proc_area.wait( timeout=60 ) # Seconds
  except TimeoutError:
    proc_area.kill()
    test_timeout = True
    
  # timeout error
  if ( test_timeout ):
    print('Timeout error: java took longer than 60 seconds to complete.')
    print('')
    test_case['feedback'] = 'Test timed out; took longer than 60 seconds to test Rectangle area'
  else:
    proc_area.poll()
    # runtime error
    if ( proc_area.returncode != 0 ):
      print('Error: java return code non-zero')
      print('Program output:')
      print('-' * 10)
      with open(area_output.name, 'r') as f:
        for line in f:
          print(line.rstrip())
      print('-' * 10)
      print('Review the java output above to diagnose error')
      print('')
      test_case['feedback'] += 'Error with Rectangle.getArea()\n'
    else:
      print('Rectangle.getArea() test successful')
      print('')
      test_case['points_earned'] += test_case['points_possible'] / 3
      
  ## Perimeter test
  print('Testing Rectangle.getPerimeter()...')
  
  perim_output = tempfile.NamedTemporaryFile()
  
  test_timeout = False
  # $ java TestShapes rectangle-area
  proc_perim = Popen( ['java', 'TestShapes', 'rectangle-perim'],
                      stdout=perim_output,
                      stderr=STDOUT,
                      text=True )
  try:
    proc_perim.wait( timeout=60 ) # Seconds
  except TimeoutError:
    proc_perim.kill()
    test_timeout = True
    
  # timeout error
  if ( test_timeout ):
    print('Timeout error: java took longer than 60 seconds to complete.')
    print('')
    test_case['feedback'] = 'Test timed out; took longer than 60 seconds to test Rectangle perimeter'
  else:
    proc_perim.poll()
    # runtime error
    if ( proc_perim.returncode != 0 ):
      print('Error: java return code non-zero')
      print('Program output:')
      print('-' * 10)
      with open(perim_output.name, 'r') as f:
        for line in f:
          print(line.rstrip())
      print('-' * 10)
      print('Review the java output above to diagnose error')
      print('')
      test_case['feedback'] += 'Error with Rectangle.getPerimeter()'
    else:
      print('Rectangle.getPerimeter() test successful')
      test_case['points_earned'] += test_case['points_possible'] / 3  
      
  ## Check if all three passed
  if ( test_case['points_earned'] == test_case['points_possible'] ):
    test_case['test_passed'] = True
  else:
    print('Failures in this test likely mean the FunWithShapes test will also fail.')
    
  # Fix the float type
  test_case['points_earned'] = int( test_case['points_earned'] )
    
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