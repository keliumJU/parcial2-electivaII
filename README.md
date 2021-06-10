# parcial3-electivaII


# Control de Asistencia API, con Arquitectura Hexagonal 

El código fuente de este repositorio es una **Refactorización** de https://github.com/keliumJU/control_de_asistencia.git, 
donde se implementó la *arquitectura hexagonal* a nivel de **API** junto con el patrón *DTO* y *SOLID*.

Es decir que se subdivido la lógica del negocio por medio de ***apps, dominios e inyección de dependencias***.

Dando como resultado una API completamente funcional que abarca 6 módulos los cuales son: 
* Estudiantes
* Semestres
* EspaciosAcademicos
* EstudiantesEspaciosAcademicos
* Sesiones
* Asistencia. 

Se puede probar los endpoints libremente utilizando el archivo **.json** importándolo en tu cliente API  preferido como **postman** o **insomnia**.
