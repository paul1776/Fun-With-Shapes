import java.lang.Math;
import java.util.*;

public class Rectangle extends Shape {

    protected Vector<Double> rectangleD;

    Rectangle( ShapeDescription description ) {
        super(description);

        rectangleD = description.getDoubles();
    }

    public double getArea() {
        return (rectangleD.get(0) * rectangleD.get(1));
    }

    public double getPerimeter() {
        return (rectangleD.get(0) * 2 + rectangleD.get(1) * 2);
    }
}