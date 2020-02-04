
public abstract class Shape {

	/**
	 * You should override this to create a shape, based on the
	 * shape's description (see ShapeDescription class)
	 * @param description the name of the shape and some doubles that define it
	 */
	Shape( ShapeDescription description ) {}
	
	/**
	 * Returns the area of a shape
	 * @return the area
	 */
	public abstract double getArea();
	
	
	/**
	 * Returns the perimeter of a shape
	 * @return the perimeter 
	 */
	public abstract double getPerimeter();
}
