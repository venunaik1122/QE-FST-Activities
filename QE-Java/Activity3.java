package com.example;

public class Activity3 {
    public static void main(String[] args) {
        
    
    double seconds = 1000000000;
    double EarthSeconds = 31557600;
    double mercuryseconds = 0.2408467;
    double venusseconds =0.61519726;
    double marsseconds = 1.8808158;
    double jupiterseconds = 11.862615;
    double satrunseconds = 84.016846;
    double uranusseconds = 84.016846;
    double neptuneseconds = 164.79132;
    System.out.println("age on the earth is "+seconds/(EarthSeconds * mercuryseconds));
    System.out.println("age on the venus is "+seconds/(EarthSeconds * venusseconds));
    System.out.println("age on the venus is "+seconds/(EarthSeconds * marsseconds));
    System.out.println("age on the venus is "+seconds/(EarthSeconds * jupiterseconds));
    
    

}
}
