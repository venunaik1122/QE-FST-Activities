package com.example;

public class Activity2 {
    public static void main(String[] args) {
        int[] arr = {10,77,10,54,-11,10};
        int sum =0;
        for(int num: arr){
            if(num==10){
                sum +=10;
            }
        }
        if (sum==30){
            System.out.println(sum);
        }
        else{
            System.out.println("invalid sum : "+ sum);
        }
    }
    
}
