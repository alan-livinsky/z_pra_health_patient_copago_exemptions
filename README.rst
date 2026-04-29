Z PRA Health — Exenciones de Copago del Paciente
=================================================

Módulo personalizado para GNU Health (Tryton 6.0) que agrega marcadores de
exención de copago directamente al registro del paciente.

Descripción
-----------

Este módulo extiende el modelo ``gnuhealth.patient`` con seis campos booleanos
que indican si el paciente está exento del pago de copago por alguna de las
causas reconocidas. Los campos se muestran en una sección dedicada
**"Exenciones de copago"** dentro del formulario del paciente, ubicada
inmediatamente después del grupo de marcadores críticos del paciente.

Campos agregados
----------------

+--------------------------------+------------------------------+
| Campo (técnico)                | Etiqueta en pantalla         |
+================================+==============================+
| ``copago_exempt_pregnant``     | Persona embarazada           |
+--------------------------------+------------------------------+
| ``copago_exempt_disabled``     | Persona discapacitada        |
+--------------------------------+------------------------------+
| ``copago_exempt_oncology``     | Paciente oncológico          |
+--------------------------------+------------------------------+
| ``copago_exempt_gynecology``   | Paciente ginecológico        |
+--------------------------------+------------------------------+
| ``copago_exempt_under_one_year`` | Menor a un año             |
+--------------------------------+------------------------------+
| ``copago_exempt_recent_surgery`` | Cirugía reciente           |
+--------------------------------+------------------------------+

Control de acceso
-----------------

Por defecto **ningún usuario** puede ver ni modificar estos campos.
Solo los miembros del grupo ``z_gestor_exepciones`` tienen permisos de
lectura y escritura sobre todos los campos de exención.

Para que un usuario pueda gestionar exenciones de copago debe ser agregado
al grupo ``z_gestor_exepciones`` desde la administración de usuarios de
Tryton (Administración → Usuarios → Grupos).

Dependencias
------------

* ``health`` (GNU Health)

Instalación
-----------

1. Copiar la carpeta del módulo al directorio de módulos de Tryton::

       cp -r z_001_copago_exemptions \
           <tryton_modules_dir>/

2. Reiniciar el servidor Tryton.

3. Desde el cliente Tryton, ir a **Administración → Módulos → Módulos**,
   buscar ``z_001_copago_exemptions`` y hacer clic en
   *Instalar*.

4. Actualizar la base de datos cuando el asistente lo solicite.

5. Agregar los usuarios correspondientes al grupo ``z_gestor_exepciones``.

Licencia
--------

GPL-3
