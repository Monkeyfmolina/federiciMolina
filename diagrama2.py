class Usuario:
    def __init__(self, nombre, email, contrasena):
        self.nombre = nombre
        self.email = email
        self.contrasena = contrasena

    def iniciar_sesion(self):
        pass

    def actualizar_perfil(self):
        pass

    def cambiar_contrasena(self):
        pass

    def ver_mensajes(self):
        pass

    def enviar_mensajes(self):
        pass

class Paciente(Usuario):
    def crear_cita(self):
        pass

    def actualizar_informacion_medica(self):
        pass

    def ver_recetas(self):
        pass

    def ver_pruebas_medicas(self):
        pass

    def generar_factura(self):
        pass

class Doctor(Usuario):
    def consultar_citas(self):
        pass

    def actualizar_generar_recetas(self):
        pass

    def ver_informacion_medica_paciente(self):
        pass

class Laboratorio(Usuario):
    def subir_pruebas_medicas(self):
        pass

class Quimico(Usuario):
    def actualizar_estado_entrega_medicamentos(self):
        pass

class Administrador(Usuario):
    def agregar_medico_laboratorio_quimico(self):
        pass

    def agregar_eliminar_especialidad_sintomas(self):
        pass

    def agregar_hospital(self):
        pass

    def ver_actividad(self):
        pass

    def ver_estadisticas_sistema(self):
        pass

    def restaurar_usuarios_archivados(self):
        pass

class Cita:
    def __init__(self, fecha_hora, paciente, doctor):
        self.fecha_hora = fecha_hora
        self.paciente = paciente
        self.doctor = doctor

class Receta:
    def __init__(self, fecha, medicamento, doctor, paciente):
        self.fecha = fecha
        self.medicamento = medicamento
        self.doctor = doctor
        self.paciente = paciente

class PruebaMedica:
    def __init__(self, fecha, tipo, paciente, laboratorio):
        self.fecha = fecha
        self.tipo = tipo
        self.paciente = paciente
        self.laboratorio = laboratorio

class Mensaje:
    def __init__(self, contenido, remitente, destinatario):
        self.contenido = contenido
        self.remitente = remitente
        self.destinatario = destinatario

class Factura:
    def __init__(self, fecha, receta):
        self.fecha = fecha
        self.receta = receta
