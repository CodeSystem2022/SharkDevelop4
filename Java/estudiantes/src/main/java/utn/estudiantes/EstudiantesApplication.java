package utn.estudiantes;

import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import utn.estudiantes.servicio.EstudianteServicio;

import java.util.logging.Logger;

@SpringBootApplication
public class EstudiantesApplication implements CommandLineRunner {
	@Autowired
	private EstudianteServicio estudianteServicio;
	private static final Logger logger = (Logger) LoggerFactory.getLogger(EstudiantesApplication.class);
	String nl = System.lineSeparator();
	public static void main(String[] args) {

		logger.info("Iniciando aplicación");
		SpringApplication.run(EstudiantesApplication.class, args);
		logger.info("Aplicación finalizada");
	}


	@Override
	public void run(String... args) throws Exception {
		logger.info(nl + "Ejecutando metodo de Spring" + nl);
	}
}
