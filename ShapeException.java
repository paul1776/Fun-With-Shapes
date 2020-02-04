/**
 * This is a new type of exception, dedicated exclusively
 * to this COSC150 homework assignment.
 * 
 * @author msherr
 */
public class ShapeException extends Exception {

	/**
	 * satisfies a compiler warning; ignore this
	 */
	private static final long serialVersionUID = 1L;

	ShapeException() {
		super();
	}
	
	ShapeException( String description ) {
		super(description);
	}
	
}
