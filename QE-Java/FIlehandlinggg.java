package Activity14;
import java.io.File;
import java.io.IOException;
import org.apache.commons.io.FileUtils;

public class FIlehandlinggg {
    public static void main(String[] args) {
        try {
            File file = new File("sample.txt");
            boolean fStatus = file.createNewFile();
            if(fStatus){
                System.out.println("file created succesfully");
            }
            else{
                System.out.println("file already exists");
            }
            FileUtils.writeStringToFile(file, "hello this is activity 14");
        } catch (Exception e) {
        }
    }

}
