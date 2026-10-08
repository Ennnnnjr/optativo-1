# ejercicio 9
class Turno:
    def __init__(self, paciente, hora):
        self.paciente = paciente
        self.hora = hora
        self.estado = "pendiente"  # Estado inicial 

    def marcar_como_atendido(self):
        """Cambia el estado del turno a atendido."""
        self.estado = "atendido"

    def __str__(self):
        return f"[{self.hora}] Paciente: {self.paciente} | Estado: {self.estado}"


class Agenda:
    def __init__(self):
        self.turnos = []  
    def agendar_turno(self, turno):
        """Añade un nuevo turno a la agenda."""
        self.turnos.append(turno)

    def listar_pendientes(self):
        """Recorre los turnos y muestra únicamente los que están pendientes."""
        print("--- TURNOS PENDIENTES ---")
        pendientes = [turno for turno in self.turnos if turno.estado == "pendiente"]
        
        if not pendientes:
            print("No hay turnos pendientes.")
            return

        for turno in pendientes:
            print(turno)


# Ejemplo

# la agenda
agenda = Agenda()

# y agendamos
turno1 = Turno("Santiago Rojas", "09:00")
turno2 = Turno("Andy Gamarra", "09:30")
turno3 = Turno("Ana Campos", "10:00")
turno4 = Turno("Juan Jimenez", "10:30")

agenda.agendar_turno(turno1)
agenda.agendar_turno(turno2)
agenda.agendar_turno(turno3)
agenda.agendar_turno(turno4)

# marcamos unos turnos
turno1.marcar_como_atendido()
turno3.marcar_como_atendido()

# mostramos los que quedan pendientes
agenda.listar_pendientes()