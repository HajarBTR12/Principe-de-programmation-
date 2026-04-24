import javax.xml.ws.Endpoint;

public class Application {
    public static void main(String[] args) {
        System.out.printf("Début de deploiment de mon service ");
        String url = "http://localhost:888/";
        Endpoint.publish(url, new MonServiceWeb());
        System.out.println("Le service web est déployé");
    }
}
