package Demos;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Activity6 {

    public static void main(String[] args) {

        
    WebDriver driver = new FirefoxDriver();
    driver.get("https://cklabs.com");

    WebElement  ele1 = driver.findElement(By.cssSelector("a.avia-button"));

    System.out.println(ele1);


    // List<WebElement> headerlinks = driver.findElements(By.className("main_menu"));

    // System.out.println("header links size : " +headerlinks.size());


    // List<WebElement> links = driver.findElements(By.tagName("a"));

    // System.out.println("Total links size : " +links.size());


    driver.quit();


        
    }

    
}
