from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Endereco(BaseModel):
    cep: str
    logradouro: str
    bairro: str
    cidade: str
    estado: str

@app.get("/endereco/{cep}", response_model=Endereco, status_code=200)
async def get_endereco(cep: str):
    # Simulação de busca do endereço no correio
    if cep == "12345-678":
        return Endereco(cep="12345-678", logradouro="Rua Exemplo", bairro="Bairro Teste", cidade="Cidade Exemplo", estado="SP")
    else:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")

@app.exception_handler(404)
async def not_found_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"message": "Endereço não encontrado"})