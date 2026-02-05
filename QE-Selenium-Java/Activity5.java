package Demos;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Activity5 {

    public static void main(String[] args) {
        
        WebDriver driver = new FirefoxDriver();

        driver.get("https://training-support.net/webelements/dynamic-controls");

        System.out.println("title of the page: "+ driver.getTitle());

        WebElement ele1 = driver.findElement(By.xpath("//input[@id ='checkbox']"));

        System.out.println("check box visible: "+ele1.isDisplayed());

        WebElement ele2 = driver.findElement(By.xpath("//button[@class = 'svelte-sfj3o4']"));

        ele2.click();

        System.out.println("check box visible: "+ele1.isDisplayed());


        driver.quit();




        

        


    }
    
}
