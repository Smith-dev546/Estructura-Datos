# 1. TUPLA: Datos fijos del evento (Inmutables)
evento_info = ("Conferencia UNIVO_Tech 2026", "30 de Agosto", "Auditorio UNIVO")

# 2. LISTA: Agenda de expositores (El orden importa y puede cambiar)
agenda_expositores = ["Pepito Fuentes", "Panchito vasquez", "Jose Martinez"]
agenda_expositores.append("María Hernandez")  # Añadimos un expositor al final

# 3. SET: Registro de asistentes únicos (No permite duplicados)
asistentes_registrados = {"Pedro", "Sofía", "Juan"}
asistentes_registrados.add("Sofía")  # Intentamos duplicar a Sofía (el set la ignorará)
asistentes_registrados.add("Elena")  # Añadimos un nuevo asistente

# --- MOSTRAR LOS DATOS ---
print("--- INFORMACIÓN DEL EVENTO ---")
print(f"Evento: {evento_info[0]} | Fecha: {evento_info[1]} | Lugar: {evento_info[2]}")

print("\n--- AGENDA DE EXPOSITORES ---")
print(" 1. ", agenda_expositores[0])
print(" 2. ", agenda_expositores[1])
print(" 3. ", agenda_expositores[2])
print(" 4. ", agenda_expositores[3])

print("\n--- LISTA DE ASISTENTES ÚNICOS ---")
print(", ".join(asistentes_registrados))
