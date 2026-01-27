package com.example;

public class Car {
    String color ;
    int make;
    String transmission;
    int tyres;
    int doors;

    public Car(){
        tyres = 4;
        doors =4;
    }
    

    public void  displaycharacterstics(){
        System.out.println(color + " \n"+make + " \n" +transmission+" \n"+tyres +" \n"+ doors);
    }
    public void accelerate(){
        System.out.println("Car is Moving forward");

    }
    public void brake(){
        System.out.println("car has stopped");
    }


}
