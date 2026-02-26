import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;

//SOAP : SIMPLE Objecte ZAccess Prtocol
//JAX-WS (Java Annotation XML for Web Service)
//JAXB (java Architcture XML Building)
//URL : Uniforme Resource Locator (QUAND ON MIS WWW )
//URN : Uniforme resource Names
//URI : Uniforme resource identifier
//URN +URL =URI

@WebService(targetNamespace = "http://www.polytech.fr")// la seule anotation pour que  notre classe soit exposer sous forme dun site web
public class MonServiceWeb {
    @WebMethod(operationName = "convertir")
    public double conversion(double mt)
    {
        return mt*0.9;

    }
    public double somme(@WebParam(name = "parametre1") double a, double b){

        return a+b;
    }

    public Etudiant getEtudiant(int identifiant){
        return new Etudiant(1, "Mario", 19);

    }
}
