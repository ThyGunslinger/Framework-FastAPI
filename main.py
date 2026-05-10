from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

app = FastAPI()

usuarios = []
medicos = []

class Usuario(BaseModel):
    id: int
    nombre: str
    email: str

class Medico(BaseModel):
    id: int
    nombre: str
    especialidad: str
    email: str

@app.post("/medicos")
def crear_medico(medico: Medico):
    medicos.append(medico)
    return {"mensaje": "Médico creado exitosamente", "medico": medico}

@app.get("/medicos")
def obtener_medicos():
    return medicos

@app.get("/medicos/{medico_id}")
def obtener_medico(medico_id: int):
    for medico in medicos:
        if medico.id == medico_id:
            return medico
    raise HTTPException(status_code=404, detail="Médico no encontrado.")

@app.put("/medicos/{medico_id}")
def actualizar_medico(medico_id: int, medico_actualizado: Medico):
    for index, medico in enumerate(medicos):
        if medico.id == medico_id:
            medicos[index] = medico_actualizado
            return {"mensaje": "Médico actualizado exitosamente", "medico": medico_actualizado}
    raise HTTPException(status_code=404, detail="Médico no encontrado.")

@app.delete("/medicos/{medico_id}")
def eliminar_medico(medico_id: int):
    for i, medico in enumerate(medicos):
        if medico.id == medico_id:
            medicos.pop(i)
            return {"mensaje": "Médico eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Médico no encontrado.")

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return {"mensaje": "Usuario creado exitosamente", "usuario": usuario}

@app.get("/usuarios")
def obtener_usuarios():
    return usuarios

@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado.")

@app.put("/usuarios/{usuario_id}")
def actualizar_usuario(usuario_id: int, usuario_actualizado: Usuario):
    for index, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            usuarios[index] = usuario_actualizado
            return {"mensaje": "Usuario actualizado exitosamente", "usuario": usuario_actualizado}
    raise HTTPException(status_code=404, detail="Usuario no encontrado.")

@app.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    for i, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            usuarios.pop(i)
            return {"mensaje": "Usuario eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado.")