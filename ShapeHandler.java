import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Vector;


public abstract class ShapeHandler {
	
	protected Vector<ShapeDescription> shapeDescriptions;
	protected Vector<Shape> shapes;
	
	
	/**
	 * Populates the shapeDefinitions vector with
	 * some definitions of shapes.  You'll need to implement 
	 * the convertDescriptionsToShapes function to actually convert
	 * these descriptions to useful shapes.
	 * 
	 * @param filename the file containing the definitions of the shapes
	 */
	ShapeHandler() throws ShapeException {
		String filename = "shapes.txt";
		shapes = new Vector<Shape>();
		shapeDescriptions = new Vector<ShapeDescription>();

		try {
			String line;
			BufferedReader reader = new BufferedReader(new FileReader(new File(filename)));
			while ((line = reader.readLine()) != null) {
				ShapeDescription description = new ShapeDescription(line);
				shapeDescriptions.add(description);				
			}			
			reader.close();
		} catch (FileNotFoundException e) {
			throw new ShapeException( "File not found" );
		} catch (IOException e) {
			throw new ShapeException( "Read failed" );
		}
		convertDescriptionsToShapes();
	}

	
	/**
	 * Given the shapeDescriptions, converts it to a vector
	 * of actual shape objects.
	 */
	public abstract void convertDescriptionsToShapes();

	
	
	/**
	 * Computes the sum of the shapes' areas, where the shapes
	 * are from the shapes list
	 * @return the sum of the shapes' areas
	 */
	public abstract double sumOverAreas();
	

	
	/**
	 * Computes the sum of the shapes' perimeters, where the shapes
	 * are from the shapes list
	 * @return the sum of the shapes' perimeters
	 */
	public abstract double sumOverPerimeters(); 

}
