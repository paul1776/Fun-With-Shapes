import java.lang.Math;
import java.util.*;

public class Triangle extends Shape {

    protected Vector<Double> triangleD;

    Triangle( ShapeDescription description ) {
        super(description);

        triangleD = description.getDoubles();
    }

    public double getArea() {
        double p = getPerimeter() / 2;
        double area = Math.sqrt(p * (p - triangleD.get(0)) * (p - triangleD.get(1)) * (p - triangleD.get(2)));
        return area;
    }

    public double getPerimeter() {
        return (triangleD.get(0) + triangleD.get(1) + triangleD.get(2));
    }
}