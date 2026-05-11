from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel


app = FastAPI()

usuarios = []

class Usuario(BaseModel):
    id: int
    nombre: str
    email: str

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