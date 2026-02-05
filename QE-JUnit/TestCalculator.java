package demo;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class TestCalculator {
    

    public  Calculator calculator;

    @BeforeAll
    public static void initAll(){
        System.out.println("Starting all the testcases..!");
    }

    @BeforeEach
    public void setup(){
        calculator = new Calculator();
    }


    @Test
    public void testAdd(){
        assertEquals(7, calculator.add(2,5));
    }
    @Test
    
    public void testMul(){
        assertEquals(6, calculator.mulitply(2, 3));
    }

    @Test
    public void testsub(){
        assertEquals(6, calculator.sub(11,1));
        
    }
    
    
}
