package utn.estudiantes.servicio;

import org.springframework.stereotype.Service;
import utn.estudiantes.modelo.Estudiante;

import java.util.List;


public interface IEstudianteServicio {
    public List<Estudiante> listarEstudiantes();

    public Estudiante obtenerEstudiante(Long id);
    public void guardarEstudiante(Estudiante estudiante);
    public void eliminarEstudiante(Long id);

}
