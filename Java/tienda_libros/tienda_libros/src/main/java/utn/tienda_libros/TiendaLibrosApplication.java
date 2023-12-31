package utn.tienda_libros;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.context.ConfigurableApplicationContext;
import utn.tienda_libros.vista.LibroFrom;

import java.awt.EventQueue;

@SpringBootApplication
public class TiendaLibrosApplication {

	public static void main(String[] args) {

		//instanciamos app string
		ConfigurableApplicationContext contextoSpring =
				new SpringApplicationBuilder(TiendaLibrosApplication.class)
						.headless(false)
						.web(WebApplicationType.NONE)
						.run(args);
		//ejecutamos el codigo para cargar el formulario
		EventQueue.invokeLater(() -> { //Metodo Lambda
			//obtenemos el evento from a traves del sprig
			LibroFrom librofrom = contextoSpring.getBean(LibroFrom.class);
			librofrom.setVisible(true);
		});
	}
}
