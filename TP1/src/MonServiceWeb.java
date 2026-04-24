import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;

//SOAP : SIMPLE Object Access Protocol
//JAX-WS (Java Annotation XML for Web Service)
//JAXB (Java Architecture XML Building)
//URL : Uniforme Resource Locator
//URN : Uniforme Resource Names
//URI : Uniforme Resource Identifier
//URN + URL = URI

@WebService(targetNamespace = "http://www.polytech.fr")
public class MonServiceWeb {

    @WebMethod(operationName = "convertir")
    public double conversion(double mt) {
        return mt * 0.9;
    }

    public double somme(@WebParam(name = "parametre1") double a, double b) {
        return a + b;
    }

    public Etudiant getEtudiant(int identifiant) {
        return new Etudiant(1, "Mario", 19);
    }
}
