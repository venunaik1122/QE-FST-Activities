package com.example.Activity7;

interface BicycleParts{
    int tyres =2;
    int maxspeed = 120;
}

interface BicycleOperations{
    void applybreak(int decrement);
    void speedup(int increment);
}

class Bicycle implements BicycleParts,BicycleOperations{
    int gears;
    int CurrentSpeed;
    Bicycle(int gears, int CurrentSpeed){
        this.gears = gears;
        this.CurrentSpeed =CurrentSpeed;
    }
    
    public void applybreak(int decrement){
        CurrentSpeed = CurrentSpeed - decrement;
    }

    public void speedup(int increment){
        CurrentSpeed = CurrentSpeed + increment;
    }

    public String BicycleDesc(){
        return "No of gears are" + gears + "\nspeed of the bicycle is"+ maxspeed;
    }
}

class MountainBike extends Bicycle{
    int seatHeight;
    MountainBike(int gears, int CurrentSpeed, int seatHeight){
        super(gears,CurrentSpeed);
        this.seatHeight = seatHeight;
    }
    public void seatHeight(int newvalue){
        seatHeight = newvalue;
    }
    @Override
    public String BicycleDesc(){
        return super.BicycleDesc() + "\nseat height is "+ seatHeight;
    }
}
public class Main{
    public static void main(String[] args) {
        MountainBike mb = new MountainBike(3, 0, 25);
        System.out.println(mb.BicycleDesc());
        mb.speedup(20);
        mb.applybreak(5);
        System.out.println("current speed:" +mb.CurrentSpeed);
    }
}

