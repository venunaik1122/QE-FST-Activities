package com.Activity11;
import java.util.HashMap;
import java.util.Map;

public class Mapping {
    public static void main(String[] args) {
        Map<Integer, String> colors = new HashMap<>();
        colors.put(1,"red");
        colors.put(2,"pink");
        colors.put(3,"black");
        colors.put(4,"white");
        colors.put(5,"green");


        System.out.println(colors.size());
        colors.remove(3);
        System.out.println(colors.containsKey(3));
        System.out.println(colors.size());
    }

}
