package com.Activity9;
import java.util.ArrayList;

public class Activity {

    public static void main(String[] args) {
        ArrayList<String> mylist = new ArrayList<>();

        mylist.add("venu");
        mylist.add("bobby");
        mylist.add("varun");
        mylist.add("swathi");
        mylist.add("keerthi");
        System.out.println("All names of the list:" );
        for (int i = 0; i < mylist.size(); i++) {
             System.out.println(mylist.get(i));
        }

            System.out.println("doesnot exist"+ mylist.contains("varun"));
            System.out.println("number of names in the list"+ mylist.size());
            mylist.remove("venu");
            System.out.println("list of names after the remove "+mylist.size());
            
        }

    }


