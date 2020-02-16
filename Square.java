import java.lang.Math;
import java.util.*;

public class Square extends Shape {

    protected Vector<Double> squareD;

    Square( ShapeDescription description ) {
        super(description);

        squareD = description.getDoubles();
    }

    public double getArea() {
        return (squareD.get(0) * squareD.get(0));
    }

    public double getPerimeter() {
        return (squareD.get(0) * 4);
    }
}