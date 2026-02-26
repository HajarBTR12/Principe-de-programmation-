import javax.xml.ws.Endpoint;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Application {
    public static void main(String[] args) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        System.out.printf("Début de deploiment de mon service ");
        String url = "http://localhost:888/";
        Endpoint.publish(url, new MonServiceWeb());// pour publier
        System.out.println ("Le service web est déployé");



    }
}