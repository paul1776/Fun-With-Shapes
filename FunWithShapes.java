import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Vector;

public class FunWithShapes extends ShapeHandler {

    FunWithShapes() throws ShapeException {
        super();
    }

    public void convertDescriptionsToShapes() {
        for (int i = 0; i < shapeDescriptions.size(); i++) {
            ShapeDescription current = shapeDescriptions.get(i);
            if ((current.getShapeType()).name() == "SQUARE") {
                Square square = new Square(current);
                shapes.add(square);
            } else if ((current.getShapeType()).name() == "CIRCLE") {
                Circle circle = new Circle(current);
                shapes.add(circle);
            } else if ((current.getShapeType()).name() == "RECTANGLE") {
                Rectangle rectangle = new Rectangle(current);
                shapes.add(rectangle);
            } else if ((current.getShapeType()).name() == "TRIANGLE") {
                Triangle triangle = new Triangle(current);
                shapes.add(triangle);
            }
        }
    }

    public double sumOverAreas() {
        double totalSum = 0;
        for (int i = 0; i < shapes.size(); i++) {
            totalSum += shapes.get(i).getArea();
        }
        return totalSum;
    }

    public double sumOverPerimeters() {
        double totalSum = 0;
        for (int i = 0; i < shapes.size(); i++) {
            totalSum += shapes.get(i).getPerimeter();
        }
        return totalSum;
    }

    public static void main(String[] args) {
        try {
            FunWithShapes fun = new FunWithShapes();
            System.out.println(fun.sumOverAreas());

        } catch (ShapeException e) {
            System.out.println("Shape Exception: ");
            System.out.print(e);
        }
    }
}