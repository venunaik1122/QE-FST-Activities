package com.Activity10;

import java.util.HashSet;

public class Hashhhh {
    public static void main(String[] args) {
        HashSet<Integer> hs = new HashSet<>();

        hs.add(1);
        hs.add(2);
        hs.add(3);
        hs.add(4);
        hs.add(5);

        System.out.println("Size of Hashset: "+ hs.size());
        hs.remove(1);
        System.out.println(hs.contains(2));
        System.out.println();
        System.out.println(hs.size());
    }
}
