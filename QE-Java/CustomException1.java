package com.example.Activity8;

class CustomException extends Exception{
    private String message;

    public CustomException(String message){
        this.message = message;
    }
    @Override
    public String getMessage(){
        return message;
    }
}

public class CustomException1 {
    public static void exceptionTest(String value) throws CustomException{
        if (value == null){
            throw new CustomException("Error: String value cannot be null");
        }
        else{
            System.out.println(value);
        }
    }
    public static void main(String[] args) {
        try {
            
            exceptionTest("will print to console");
            exceptionTest(null);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
    }


}
