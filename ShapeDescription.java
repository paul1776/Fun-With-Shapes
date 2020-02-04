import java.util.Vector;

public class ShapeDescription {

	public enum ShapeTypes {
		CIRCLE,
		SQUARE,
		RECTANGLE,
		TRIANGLE
	}
	
	private ShapeTypes shapeType;
	private Vector<Double> doubles;
	
	/**
	 * Given a line from a file, parse it into a shape
	 * @param line
	 */
	ShapeDescription( String line ) throws ShapeException {
		doubles = new Vector<Double>();
		try {
			String[] parts = line.split(" ");
			if (parts[0].equalsIgnoreCase("circle")) {
				shapeType = ShapeTypes.CIRCLE;
				Double radius = Double.valueOf(parts[1]);
				doubles.add(radius);
			} else if (parts[0].equalsIgnoreCase("square")) {
					shapeType = ShapeTypes.SQUARE;
					Double sidelen = Double.valueOf(parts[1]);
					doubles.add(sidelen);
			} else if (parts[0].equalsIgnoreCase("rectangle")) {
				shapeType = ShapeTypes.RECTANGLE;
				Double width = Double.valueOf(parts[1]);
				Double height = Double.valueOf(parts[2]);
				doubles.add(width);
				doubles.add(height);
			} else if (parts[0].equalsIgnoreCase("triangle")) {
				shapeType = ShapeTypes.TRIANGLE;
				Double sideA = Double.valueOf(parts[1]);
				Double sideB = Double.valueOf(parts[2]);
				Double sideC = Double.valueOf(parts[3]);
				doubles.add(sideA);
				doubles.add(sideB);
				doubles.add(sideC);
			} else {
				throw new ShapeException( "Invalid shape name" );
			}
		} catch( ArrayIndexOutOfBoundsException e ) {
			throw new ShapeException( "Invalid shape definition" );
		} catch( Exception e ) {
			throw new ShapeException();
		}
	}
	
	
	/**
	 * @return the shapeType
	 */
	public ShapeTypes getShapeType() {
		return shapeType;
	}

	/**
	 * @return the doubles
	 */
	public Vector<Double> getDoubles() {
		return doubles;
	}


	
}
