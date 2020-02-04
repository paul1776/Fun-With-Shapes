# Programming Assignment 2: Fun With Shapes
## COSC 150 - Advanced Programming

- [Goals](#goals)
- [Description](#description)
- [Specification and requirements](#specification-and-requirements)
- [Provided files](#provided-files)
- [Grading rubric](#grading-rubric)

## Goals

In order to complete this assignment, you will need to:
- Understand how class heirarchies and relationships are expressed in UML
   - Create a UML class diagram expressing the relationships used in this assignment
- Understand Java object-oriented-programming
   - Create subclasses of existing Java classes
   - Implement the abstract methods of a parent class
   - Understand the relationship between parent and child constructors

## Description

In this assignment you will write a program, named `FunWithShapes`, which will read a text file describing different geometric shapes, convert these test descriptions into objects, and use the resulting objects to perform basic calculations.

You are provided with source code for several classes to help with this task;
namely, the abstract classes `ShapeHandler` and `Shape` which you will extend to form several subclasses.

## Specification and requirements

### Specification

You will implement a class named `FunWithShapes` whose `main` method will read in data from a text input file and populate a Vector of `Shape` objects. Your program will then sum the areas of all shapes and the perimeters of all shapes and print these results to the terminal.

The format of the input file, as well as descriptions of the provided code, are given below.

#### The input file

Data input for your program is provided by a text file, named `shapes.txt`, which must be located in your working directly. Each line of this file corresponds to a single geometric shape and will follow one of the patterns below:
- `circle <radius>` describes a circle with the given radius
- `square <sideLength>` describes a square with the given side length
- `rectangle <height> <width>` describes a rectangle of the given dimensions
- `triangle <sideA> <sideB> <sideC>` describes a triangle of the given dimensions

An example `shapes.txt` might contain the following four lines:
```
square 5
rectangle 5 10
square 3
triangle 3 4 5
```

A valid `shapes.txt` may have one line or many; it may use a particular shape type multiple times or not at all. Identical data on separate lines should be understood to be two distinct shapes (whose attributes happen to be the same).

#### The `ShapeHandler` class

The abstract class `ShapeHandler` contains the following members:
- Member fields
   - `Vector<ShapeDescription> shapeDescriptions` stores `ShapeDescription` objects created by reading and parsing lines of `shapes.txt`.
   - `Vector<Shape> shapes` stores `Shape`-type objects created by parsing `ShapeDescriptions`.
- Member methods
   - `ShapeHandler()`, the default constructor, takes the following actions:
      - Opens the `shapes.txt` file
      - Reads each line of the file
      - Creates a corresponding `ShapeDescription` and stores it in the `shapeDescriptions` vector.
      - Calls `convertDescriptionsToShapes()`.
   - `convertDescriptionsToShapes()`, an *abstract* method, should: 
      - Iterate through `shapeDescriptions`
      - Instantiate an appropriate `Shape`-type object and store it in the `shapes` vector.
   - `sumOverAreas()`, an *abstract* method, should:
      - Iterate through `shapes`
      - Compute a running total of the shape areas and return the result.
   - `sumOverPerimeters()`, and *abstract* method, should:
      - Iterate through `shapes`
      - Compute a running total of the shape perimeters and return the result.

You will implement `FunWithShapes` to extend this class (and, by extension, implement the abstract methods described above).
      
#### The `Shape` class

The abstract class `Shape` contains the following member methods:
- `Shape( ShapeDescription )`, a constructor; subclasses will use the `ShapeDescription` object to initialize the appropriate member fields. (*note: Shape has no default constructor.*)
- `getArea()`, an *abstract* method which returns this shape's area.
- `getPerimeter()`, an *abstract* method which returns this shape's perimeter.

You will implement several subclasses of `Shape` corresponding to the shape types in `shapes.txt` with appropriate member fields and method implementations.

#### The `ShapeDescription` class

The class `ShapeDescription` is an intermediate representation of a shape with the following members:
- Member fields:
   - `ShapeTypes shapeType`, an enumerated value set by parsing the shape from a line of `shapes.txt`.
   - `Vector<Double> doubles` a vector of doubles matching those provided in `shapes.txt` for this shape. The number of values will depend on the shape type.
- Member methods:
   - `getShapeType()`, which returns the value of `shapeType`.
   - `getDoubles()`, which returns the vector `doubles`.
- Other members:
   - `ShapeTypes`, an enumerated type with four values:
      - `ShapeTypes.CIRCLE`
      - `ShapeTypes.SQUARE`
      - `ShapeTypes.RECTANGLE`
      - `ShapeTypes.TRIANGLE`
      The fully-qualified name for, e.g., the circle type is `ShapeDescription.ShapeTypes.CIRCLE` (for comparison in `main()`)

The provided code in `ShapeHandler` will generate these objects by parsing the `shapes.txt` file; you will use them to generate `Shape`-type objects.

#### The `ShapeException` class

This is a simple `Exception`-type object which is thrown by `ShapeHandler()` or `ShapeDescription()` in response to invalid syntax within `shapes.txt` or other I/O issues.

### Requirements

You will create the following files and add them to your repository:
- `ClassDiagram.pdf`, a UML class diagram which describes the relationships between all classes used in this project:
   - All provided classes (in the given code)
   - All classes you implement
This diagram will be *hand-graded* by me after the due date; I will use your last commit (before the deadline) when examining this file. 

- `FunWithShapes.java`, implementing the class `FunWithShapes`. This class should
   - Extend `ShapeHandler` and implement the abstract methods described above.
   - Provide a `main()` method which will
      - Instantiate a `FunWithShapes` object
      - Invoke `sumOverAreas()` on that object.
      - Invoke `sumOverPerimeters()` on that object.
      - Print these two values to the terminal (see below).
- Four source files, each implmenting a single subclass of `Shape`:
   - `Circle.java`
   - `Square.java`
   - `Rectangle.java`
   - `Triangle.java`

#### Program invocation and outputs

Your program will be executed by running the `FunWithShapes` class. It should output exactly two lines to the terminal.
- The first line should contain ONLY the sum of the areas of all shapes (i.e., the return value of `sumOverAreas()`)
- The second line should contain ONLY the sum of the perimeters of all shapes (i.e., the return value of `sumOverPerimeters()`)
Your program should not produce ANY additional output (no line labels, units, etc). Doing so will cause the test script to incorrectly parse your output as non-numeric and the test will fail.

As an example, invoking your program on the sample `shapes.txt` above would produce the following output in terminal:
```
$ java FunWithShapes
90.0
74.0
```
   
#### A useful formula for triangle area

The `shapes.txt` specification of a `Triangle` provides the lengths of the three sides, but no direct information about angles; in particular, you should not assume this is a right triangle!

You may find it helpful to consider [Heron's Formula](https://en.wikipedia.org/wiki/Heron%27s_formula) (link to Wikipedia), which provides a method of calculating triangle area using the three side lengths and the semiperimiter (the perimeter divided by two).

## Provided files

The following files are provided code for the project and already present in your repository:
- `ShapeHandler.java`
- `Shape.java`
- `ShapeDescription.java`
- `ShapeException.java`

You should not modify these files while implementing your code; doing so may cause the autograding tests to fail.

Additionally, the following files related to project logistics are present in your repository:
- `README.md` which provides this specification.
- `.gitignore` which specifies files git should NOT track.
  - Note that `shapes.txt` is specifically listed so it will NOT be added to tracking.
- `.travis.yml` which provides instructions to trigger Travis testing.
- `travis` a directory containing the testing scripts.

You should not modify *any* of these files while working on your project; doing so may break Travis such that a test build does not run, or gives false/misleading feedback about your code.

## Grading rubric

Your score for this assignment is determined according to the following rubric.

Amazing Feat | Points Awarded | Tested by TravisCI?
---          | :---:          | ---:
**Travis-graded tests**
Your repository contains at least one commit.                   | 10 | Yes
Your commit contains all the required files with correct names. | 10 | Yes
Your source code compiles.                                      | 20 | Yes
Your `Circle` class instantiates; correcly computes area, and correctly computes perimeter. | 15 | Yes
Your `Square` class instantiates; correcly computes area, and correctly computes perimeter. | 15 | Yes
Your `Rectangle` class instantiates; correcly computes area, and correctly computes perimeter. | 15 | Yes
Your `Triangle` class instantiates; correcly computes area, and correctly computes perimeter. | 15 | Yes                            |    |
The total area and perimeter reported are correct (30x random files) | 30 | Yes
**Ray-graded tests**                                            |    |
Your class diagram is legible, neatly formatted, and uses proper UML styling for classes and relationships. | 20 | *No*
**Total points**                                                | 150 |
