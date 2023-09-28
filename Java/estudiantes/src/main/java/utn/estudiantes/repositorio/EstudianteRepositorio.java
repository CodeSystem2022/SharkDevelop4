package utn.estudiantes.repositorio;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import utn.estudiantes.modelo.Estudiantes2022;

@Repository
public interface EstudianteRepositorio extends JpaRepository<Estudiantes2022, Integer> {

}
