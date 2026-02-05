
package Demos;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class NavComAct3 {

    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        driver.get("https://training-support.net/webelements/login-form");
        
        System.out.println(driver.getTitle() + " before login");

        WebElement ele1 = driver.findElement(By.xpath("//input[@id='username']"));
        ele1.sendKeys("admin");

        WebElement ele2 = driver.findElement(By.xpath("//input[@id='password']"));
        ele2.sendKeys("password");

        WebElement ele3 = driver.findElement(By.xpath("//button[@class='svelte-1pdjkmx']"));
        ele3.click();

        System.out.println(driver.getTitle() + " after login");

        driver.quit();
    }
}
