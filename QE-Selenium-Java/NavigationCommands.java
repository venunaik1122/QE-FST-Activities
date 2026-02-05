package Demos;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class NavigationCommands {

    public static void main(String[] args){
        WebDriver driver = new FirefoxDriver();

        driver.get("https://training-support.net/webelements/target-practice");


        System.out.println("title: " + driver.getTitle());

        WebElement ele1 = driver.findElement(By.className("text-sky-600"));

        System.out.println("h1: "+ ele1.getText());

        WebElement ele2 = driver.findElement(By.xpath("//button[@class ='rounded-xl bg-purple-200 p-2 text-3xl font-bold text-purple-900 svelte-2hb4ib']"));

        System.out.println("color :"+ ele2.getCssValue("color"));


        driver.quit();

 




        


    }
}
    

