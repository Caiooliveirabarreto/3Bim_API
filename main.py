from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def Raiz():
    return {'mensagem':'Minha primeira API em FastAPI'}

@app.get('/clientes')
def return_clientes():
    return {'mensagem':'Lista de clientes'}

