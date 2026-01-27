package com.example.Activity6;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
 class Airport {
    private List<String>passenger;
    private int maxPassengers;
    private Date lastTimeTookOff;
    private Date lastTimeLanded;

    public Airport(int maxPassengers){
        this.maxPassengers = maxPassengers;
        this.passenger = new ArrayList<>();
    }
    public void onboard(String name){
        if(passenger.size() < maxPassengers){
            passenger.add(name);
        }
        else{
            System.out.println("plane is full!");
        }
    }
    public Date takeoff(){
        lastTimeTookOff = new Date();
        return lastTimeTookOff;
    }

    public void land(){
        lastTimeLanded = new Date();
        passenger.clear();
    }
    public Date getLastTimeLanded(){
        return lastTimeLanded;
    }

    public List<String> getPassengers(){
        return passenger;
    }
}
class Plane {
    public static void main(String[] args) throws InterruptedException {
        Airport plane = new Airport(10);
        plane.onboard("rohit");
        plane.onboard("sharukh");
        plane.onboard("sai");

        System.out.println("Take off time " + plane.takeoff());
        System.out.println("passengers onboard" + plane.getPassengers());
        Thread.sleep(5000);
        plane.land();

        System.out.println("landing time: "+ plane.getLastTimeLanded());

    }
}
