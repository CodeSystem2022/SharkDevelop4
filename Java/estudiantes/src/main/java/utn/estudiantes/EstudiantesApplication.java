package utn.estudiantes;

import org.slf4j.Logger; //es para enviar info a la consola, al usar un framework no usamos el soutpl
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import utn.estudiantes.modelo.Estudiantes2022;
import utn.estudiantes.servicio.EstudianteServicio;
import java.util.List;
import java.util.Scanner;

@SpringBootApplication
public class EstudiantesApplication implements CommandLineRunner {
	@Autowired
	private EstudianteServicio estudianteServicio; //inyrccion de dependencias
	private static final Logger logger =
			LoggerFactory.getLogger(EstudiantesApplication.class); //esto es para obtener un logger e imprimir en consola
	String nl = System.lineSeparator(); //regresa el caracter correcto para cualquier dispositivo

	public static void main(String[] args) {
		logger.info("Iniciando la aplicacion..");
		//Levantar fabrica de Spring
		SpringApplication.run(EstudiantesApplication.class, args);
		logger.info("Aplicacion finalizada");
	}


	@Override
	public void run(String... args) throws Exception {
		logger.info(nl + "Ejecutamos el metodo run..." + nl);
		var salir = false;
		var consola = new Scanner(System.in);
		while (!salir) {
			mostrarMenu();
			salir = ejecutarOpciones(consola);
			logger.info(nl);
		} //fin del while
	} //metodo run

	private void mostrarMenu() {
		//	logger.info(nl);
		logger.info("""
					  	******* Sistema de Estudiantes *******
					  	1. Lista Estudiante
					  	2. Buscar Estudiante
					  	3. Agregar Estudiante
					  	4. Modificar Estudiante
					  	5. Eliminar Estudainte
					  	6. Salir
					Eliga una opción:""");
	}


	private boolean ejecutarOpciones(Scanner consola) {
		try {
			var opcion = Integer.parseInt(consola.nextLine());
			var salir = false;
			switch (opcion) {
				case 1 -> { //Listar estudiantes
					logger.info(nl + "Listado de estudiantes: " + nl);
					List<Estudiantes2022> estudiantes = estudianteServicio.listarEstudiantes();
					estudiantes.forEach((estudiante -> logger.info(estudiante.toString() + nl)));
				}
				case 2 -> {
					logger.info("Digite el id estudiante a buscar: ");
					var idEstudiante = Integer.parseInt(consola.nextLine());
					Estudiantes2022 estudiante =
							estudianteServicio.obtenerEstudiante(idEstudiante);
					if(estudiante != null)
						logger.info("Estudiante encontrado: "+ estudiante + nl);
					else
						logger.info("Estudiante NO encontrado: "+estudiante+nl);
				}
				case 3 -> {
					logger.info("Agregar estudiante: "+nl);
					logger.info("Nombre: ");
					var nombre = consola.nextLine();
					logger.info("Apellido: ");
					var apellido = consola.nextLine();
					logger.info("Telefono: ");
					var telefono = consola.nextLine();
					logger.info("Email: ");
					var email = consola.nextLine();
					// Crear el objeto estudiante sin el id
					var estudiante = new Estudiantes2022();
					estudiante.setNombre(nombre);
					estudiante.setApellido(apellido);
					estudiante.setTelefono(telefono);
					estudiante.setEmail(email);
					estudianteServicio.guardarEstudiante(estudiante);
					logger.info("Estudiante agregado: "+estudiante+nl);
				}
				case 4 -> {
					logger.info("Modificar estudiante: " + nl);
					logger.info("Ingrese el id estudiante: ");
					var idEstudiante = Integer.parseInt(consola.nextLine());
					//buscamos el estudiante a modificar
					Estudiantes2022 estudiante =
							estudianteServicio.obtenerEstudiante(idEstudiante);
					if (estudiante != null) {
						logger.info("Nombre: ");
						var nombre = consola.nextLine();
						logger.info("Apellido: ");
						var apellido = consola.nextLine();
						logger.info("Telefono: ");
						var telefono = consola.nextLine();
						logger.info("Email: ");
						var email = consola.nextLine();
						estudiante.setNombre(nombre);
						estudiante.setApellido(apellido);
						estudiante.setTelefono(telefono);
						estudiante.setEmail(email);
						estudianteServicio.guardarEstudiante(estudiante);
						logger.info("Estudiante modificado: " + estudiante + nl);
					} else
						logger.info("Estudiante NO encontrado con el id: " + idEstudiante + nl);
				}
				case 5 -> {
					logger.info("Eliminar estudiante:  " + nl);
					logger.info("Digite el id estudiante: ");
					var idEstudiante = Integer.parseInt(consola.nextLine());
					//Buscamos el id de estudiante a eliminar
					var estudiante = estudianteServicio.obtenerEstudiante(idEstudiante);
					if (estudiante != null) {
						estudianteServicio.eliminarEstudiante(estudiante);
						logger.info("Estudiante eliminado: " + estudiante + nl);
					}
					else
						logger.info("Estudiante NO encontrado con id: " + estudiante + nl);
				}
				case 6 -> {
					logger.info("Hasta pronto: "+ opcion+nl);
					salir = true;
				}//fin case
				default -> logger.info("Opcion no reconocida: "+ opcion+ nl);
			} //fin switch
			return salir;

		} catch (NumberFormatException e) {
			System.out.println("Error: Se esperaba un entero, pero se recibió una cadena.");
		} catch (Exception e) {
			System.out.println("Se produjo un error: " + e.getMessage());
		}
		return false; // Devuelve false o algún valor predeterminado en caso de excepción
	}

}