import java.lang.Math;
import java.util.*;

public class Circle extends Shape {

    protected Vector<Double> circleD;

    Circle( ShapeDescription description ) {
        super(description);

        circleD = description.getDoubles();
    }

    public double getArea() {
        return (Math.PI * circleD.get(0) * circleD.get(0));
    }

    public double getPerimeter() {
        return (2 * Math.PI * circleD.get(0));
    }
}