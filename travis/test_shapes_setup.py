# Create TestShapes.java
# Compile TestShapes.java

with open( 'TestShapes.java', 'wt' ) as testFile:
  testFile.write("""  
import java.util.Random;

class TestShapes {
    public static void main(String[] args) throws ShapeException {

	Random rnd = new Random();
	double tolerance = 1;
	
	if (args[0].equals("circle-instantiate")) {
	    ShapeDescription desc = new ShapeDescription("circle 5.0");
	    Circle circ = new Circle(desc);
	} else if (args[0].equals("circle-area")) {
	    double radius = rnd.nextDouble() * 100.0;
	    ShapeDescription desc = new ShapeDescription("circle " + radius );
	    Circle circ = new Circle(desc);
	    double correct_area = Math.PI * radius * radius;
        double report_area = circ.getArea();
        double error = Math.abs( correct_area - report_area ) / correct_area * 100;
	    if ( error > tolerance) {
          System.out.println("Incorrect circle area (error exceeds " + tolerance + "%)");
          System.out.println("Radius: " + radius);
          System.out.println("Correct area: " + correct_area);
          System.out.println("Reported area: " + report_area );
          System.out.println("Percent error: " + error );
		  System.exit(1);
	    } else {
		  System.out.println( "Correctly computed circle area when radius = " + radius );
	    }
	} else if (args[0].equals("circle-perim")) {
	    double radius = rnd.nextDouble() * 100.0;
	    ShapeDescription desc = new ShapeDescription("circle " + radius );
	    Circle circ = new Circle(desc);
	    double correct_perim = Math.PI * radius * 2.0;
        double report_perim = circ.getPerimeter();
        double error = Math.abs( correct_perim - report_perim ) / correct_perim * 100;
	    if ( error > tolerance) {
          System.out.println("Incorrect circle perimeter (error exceeds " + tolerance + "%)");
          System.out.println("Radius: " + radius);
          System.out.println("Correct perimeter: " + correct_perim );
          System.out.println("Reported perimeter: " + report_perim );
          System.out.println("Percent error: " + error );
		  System.exit(1);
	    } else {
		  System.out.println( "Correctly computed circle perimeter when radius = " + radius );
	    }

	    
	} else if (args[0].equals("rectangle-instantiate")) {
	    ShapeDescription desc = new ShapeDescription("rectangle 5.0 10.0");
	    Rectangle rectangle = new Rectangle(desc);
	} else if (args[0].equals("rectangle-area")) {
	    double height = rnd.nextDouble() * 100.0;
	    double width = rnd.nextDouble() * 100.0;
	    ShapeDescription desc = new ShapeDescription("rectangle " + height + " " + width );
	    Rectangle rectangle = new Rectangle(desc);
	    double correct_area = height * width;
        double report_area = rectangle.getArea();
        double error = Math.abs( correct_area - report_area ) / correct_area * 100;
	    if ( error > tolerance) {
          System.out.println("Incorrect rectangle area (error exceeds " + tolerance + "%)");
          System.out.println("Dimensions: " + height + " " + width);
          System.out.println("Correct area: " + correct_area);
          System.out.println("Reported area: " + report_area );
          System.out.println("Percent error: " + error );
		  System.exit(1);
	    } else {
		System.out.println( "Correctly computed rectangle area." );
	    }
	} else if (args[0].equals("rectangle-perim")) {
	    double height = rnd.nextDouble() * 100.0;
	    double width = rnd.nextDouble() * 100.0;
	    ShapeDescription desc = new ShapeDescription("rectangle " + height + " " + width );
	    Rectangle rectangle = new Rectangle(desc);
	    double correct_perim = 2.0 * (height + width);
	    double report_perim = rectangle.getPerimeter();
        double error = Math.abs( correct_perim - report_perim ) / correct_perim * 100;
	    if ( error > tolerance) {
          System.out.println("Incorrect rectangle perimeter (error exceeds " + tolerance + "%)");
          System.out.println("Dimensions: " + height + " " + width);
          System.out.println("Correct perimeter: " + correct_perim );
          System.out.println("Reported perimeter: " + report_perim );
          System.out.println("Percent error: " + error );
		  System.exit(1);
	    } else {
		System.out.println( "Correctly computed rectangle perimeter." );
	    }


	} else if (args[0].equals("square-instantiate")) {
	    ShapeDescription desc = new ShapeDescription("square 5.0 10.0");
	    Square square = new Square(desc);
	} else if (args[0].equals("square-area")) {
	    double height = rnd.nextDouble() * 100.0;
	    ShapeDescription desc = new ShapeDescription("square " + height );
	    Square square = new Square(desc);
	    double correct_area = height * height;
	    double report_area = square.getArea();
        double error = Math.abs( correct_area - report_area ) / correct_area * 100;
	    if ( error > tolerance) {
          System.out.println("Incorrect square area (error exceeds " + tolerance + "%)");
          System.out.println("Side: " + height);
          System.out.println("Correct area: " + correct_area);
          System.out.println("Reported area: " + report_area );
          System.out.println("Percent error: " + error );
		  System.exit(1);
	    } else {
		  System.out.println( "Correctly computed square area." );
	    }
	} else if (args[0].equals("square-perim")) {
	    double height = rnd.nextDouble() * 100.0;
	    ShapeDescription desc = new ShapeDescription("square " + height );
	    Square square = new Square(desc);
	    double correct_perim = 4.0 * height;
	    double report_perim = square.getPerimeter();
        double error = Math.abs( correct_perim - report_perim ) / correct_perim * 100;
	    if ( error > tolerance) {
          System.out.println("Incorrect square perimeter (error exceeds " + tolerance + "%)");
          System.out.println("Side: " + height);
          System.out.println("Correct perimeter: " + correct_perim );
          System.out.println("Reported perimeter: " + report_perim );
          System.out.println("Percent error: " + error );
		  System.exit(1);
	    } else {
		System.out.println( "Correctly computed square perimeter." );
	    }



	} else if (args[0].equals("triangle-instantiate")) {
	    ShapeDescription desc = new ShapeDescription("triangle 3.0 4.0 10.0");
	    Triangle triangle = new Triangle(desc);
	} else if (args[0].equals("triangle-area")) {
	    
        double side1 = rnd.nextDouble() * 100.0;
        double lower = rnd.nextDouble();
        double higher = rnd.nextDouble();
        if ( lower > higher ) {
          double tmp = lower;
          lower = higher;
          higher = tmp;
        }
        double alpha = lower * Math.PI;
        double beta = (higher - lower ) * Math.PI;
        
        double side2 = side1 / 
        ( Math.cos(alpha) + Math.cos(beta) * ( Math.sin(alpha) / Math.sin(beta) ) );
        double side3 = side2 * ( Math.sin(alpha) / Math.sin(beta) );

	    ShapeDescription desc = new ShapeDescription("triangle " + side1 + " " + side2 + " " + side3 );
	    Triangle triangle = new Triangle(desc);
	    double perimeter = side1 + side2 + side3;
	    double p = perimeter / 2;
	    double correct_area = Math.sqrt( p * (p - side1) * (p - side2) * (p - side3));
	    double report_area = triangle.getArea();
        double error = Math.abs( correct_area - report_area ) / correct_area * 100;
	    if ( error > tolerance) {
          System.out.println("Incorrect triange area (error exceeds " + tolerance + "%)");
          System.out.println("Sides: " + side1 + " " + side2 + " " + side3);
          System.out.println("Correct area: " + correct_area);
          System.out.println("Reported area: " + report_area );
          System.out.println("Percent error: " + error );
		  System.exit(1);
	    } else {
		  System.out.println( "Correctly computed triangle area." );
	    }
	} else if (args[0].equals("triangle-perim")) {
	    
        double side1 = rnd.nextDouble() * 100.0;
        double lower = rnd.nextDouble();
        double higher = rnd.nextDouble();
        if ( lower > higher ) {
          double tmp = lower;
          lower = higher;
          higher = tmp;
        }
        double alpha = lower * Math.PI;
        double beta = (higher - lower ) * Math.PI;
        
        double side2 = side1 / 
        ( Math.cos(alpha) + Math.cos(beta) * ( Math.sin(alpha) / Math.sin(beta) ) );
        double side3 = side2 * ( Math.sin(alpha) / Math.sin(beta) );
	    ShapeDescription desc = new ShapeDescription("triangle " + side1 + " " + side2 + " " + side3 );
	    Triangle triangle = new Triangle(desc);
	    double correct_perim = side1 + side2 + side3;
	    double report_perim = triangle.getPerimeter();
        double error = Math.abs( correct_perim - report_perim ) / correct_perim * 100;
	    if ( error > tolerance) {
          System.out.println("Incorrect triangle perimeter (error exceeds " + tolerance + "%)");
          System.out.println("Sides: " + side1 + " " + side2 + " " + side3);
          System.out.println("Correct perimeter: " + correct_perim );
          System.out.println("Reported perimeter: " + report_perim );
          System.out.println("Percent error: " + error );
		  System.exit(1);
	    } else {
		System.out.println( "Correctly computed triangle perimeter." );
	    }

	} else {
	    System.err.println("INVALID TEST");
	    System.exit(1);
	}
	

    }
}
""")

from subprocess import Popen, PIPE, STDOUT

test_timeout = False
# $ javac <fileName>
proc_compile = Popen( ["javac", "TestShapes.java"],
                          stdout=PIPE,
                          stderr=STDOUT,
                          text=True )
    
try:
  proc_compile.wait( timeout=60 ) # Seconds
except TimeoutError:
  proc_compile.kill()
  test_timeout = True
    
compile_output = proc_compile.stdout.read()
    
# timeout error
if ( test_timeout ):
  print('Timeout error: javac took longer than 60 seconds to complete.')
# test returned
else:
  proc_compile.poll()
  # compiler error
  if ( proc_compile.returncode != 0 ):
    print('Compilation error: javac return code non-zero')
    print('Compiler output:')
    print('-' * 10)
    print( compile_output )
    print('-' * 10)
    print('Review the javac output above to diagnose compiler error')