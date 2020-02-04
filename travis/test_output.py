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
  'name' : 'Output Test',
  'description' : 'The total area and perimeter reported are correct',
  'points_possible' : 30,
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
  import random
  import math
  import tempfile
  
  print('Testing your program with randomly-generated shapes.txt files...')
  
  test_count = test_case['points_possible']
  shape_sets_per_test = 2
  tolerance = 1 # percent
  
  for tests_run in range(1,test_count+1):
  
    print('Generating shapes.txt #%i...' % tests_run)
    
    with open('shapes.txt', 'wt') as shapes:
      for set in range(0,shape_sets_per_test):
        radius = random.random() * 100.0
        side = random.random() * 100.0
        height = random.random() * 100.0
        width = random.random() * 100.0
        # Generate valid triangle
        side1 = random.random() * 100
        lower = random.random()
        upper = random.random()
        if ( lower > upper ):
          tmp = lower
          lower = upper
          upper = tmp
        alpha = lower * math.pi
        beta = (upper - lower) * math.pi
        side2 = side1 / ( math.cos(alpha) + math.cos(beta) * ( math.sin(alpha) / math.sin(beta) ) )
        side3 = side2 * ( math.sin(alpha) / math.sin(beta) )
        #
        shapes.write('circle %f\n' % radius)
        shapes.write('square %f\n' % side)
        shapes.write('rectangle %f %f\n' % (height, width) )
        shapes.write('triangle %f %f %f\n' % (side1, side2, side3) )
      # end for
    #endf file write
    
    # Compute the correct answers for this file
    totalArea = 0
    totalPerimeter = 0
    with open('shapes.txt', 'rt') as shapes:
      for line in shapes:
        line = line.strip()
        parts = line.split( ' ' )
        shape = parts[0]
        doubles = parts[1:]
        if ( shape.lower() == 'circle' ):
          radius = float(doubles[0])
          area = math.pi * radius * radius
          perimeter = 2 * math.pi * radius
        elif ( shape.lower() == 'square' ):
          side = float(doubles[0])
          area = side * side
          perimeter = 4 * side
        elif ( shape.lower() == 'rectangle' ):
          height = float(doubles[0])
          width = float(doubles[1])
          area = height * width
          perimeter = 2 * height + 2 * width
        elif ( shape.lower() == 'triangle' ):
          side1 = float(doubles[0])
          side2 = float(doubles[1])
          side3 = float(doubles[2])
          perimeter = side1 + side2 + side3
          p = perimeter / 2
          area = math.sqrt( p * (p - side1) * (p - side2) * (p - side3) )
        else:
          print('An error occurred reading this input file!')
        
        totalArea += area
        totalPerimeter += perimeter
      # end for
    # end read
    
    ## Run their code for output
    
    print('Running your code on shapes.txt #%i...' % tests_run)
    
    fws_output = tempfile.NamedTemporaryFile()
    
    # $ java FunWithShapes
    proc_fws = Popen( ['java', 'FunWithShapes'],
                      stdout=fws_output,
                      stderr=STDOUT,
                      text=True )
    
    test_timeout = False
    try:
      proc_fws.wait( timeout=60 )
    except TimeoutError:
      proc_fws.kill()
      test_timeout = True
    
    if ( test_timeout ):
      print('Timeout error: java took longer than 60 seconds to complete.')
      print('')
      print('Your program failed on the following shapes.txt:')
      print('-'*10)
      with open('shapes.txt', 'rt') as shapes:
        for line in shapes:
          print(line.strip())
        #
      #
      print('-'*10)
      break # Don't run any more tests
    else:
      proc_fws.poll()
      if ( proc_fws.returncode != 0 ):
        print('Your program exited with non-zero status')
        print('Program output:')
        with open(fws_output.name, 'r') as f:
          for line in f:
            print(line.rstrip())
        print(' ')
        break # Don't run more tests
      else:
        fws_string = ''
        with open(fws_output.name, 'r') as f:
          for line in f:
            fws_string = fws_string + line
        fws_values = fws_string.strip().split('\n')
        try:
          reportArea = float( fws_values[0] )
          reportPerimeter = float( fws_values[1] )
        except ValueError:
          print('Error parsing your program output')
          print('The first line should contain ONLY the sum of the areas of all shapes')
          print('The second line should contain ONLY the sum of the perimeters of all shapes')
          print('Your program output')
          print('-' * 10)
          print( fws_output )
          print('-' * 10)
          print('Change program output to match the specification and commit again')
          break # Don't run any more tests
        #
        errorArea = math.fabs( totalArea - reportArea ) / totalArea * 100
        errorPerimeter = math.fabs( totalPerimeter - reportPerimeter ) / totalPerimeter * 100
        
        if ( errorArea > tolerance or errorPerimeter > tolerance ):
          if ( errorArea > tolerance ):
            print('Incorrect total area (error exceeds %i%%)' % tolerance)
            print('Correct Area:', totalArea)
            print('Reported Area:', reportArea)
            print('Percent Error:', errorArea)
            print('')
          if (errorPerimeter > tolerance ):
            print('Incorrect total perimeter (error exceeds %i%%)' % tolerance)
            print('Correct Perimeter:', totalPerimeter)
            print('Reported Perimeter:', reportPerimeter)
            print('Percent Error:', errorPerimeter)
            print('')
          print('Your program failed on the following shapes.txt:')
          print('-'*10)
          with open('shapes.txt', 'rt') as shapes:
            for line in shapes:
              print(line.strip())
            #
          #
          print('-'*10)
          break # Don't run any more tests
        else:
          print('Your code succeeded with shapes.txt #%i!' % tests_run)
          test_case['points_earned'] += 1
        #
      # end else (zero return code)
    # end else (no timeout error)   
  # end for (test iteration loop)
  
  if ( test_case['points_earned'] == test_case['points_possible'] ):
    test_case['test_passed'] = True
  else:
    print('See the output above for a shapes.txt that your program handled incorrectly')  
    
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