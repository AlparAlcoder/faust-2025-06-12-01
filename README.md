# Documentação da API FastAPI

## 1. Visão geral da API
Esta API foi desenvolvida utilizando o framework FastAPI em Python. Ela fornece um endpoint para consultar informações de endereços a partir de um CEP. A API retorna um objeto contendo o logradouro, bairro, cidade e estado correspondentes ao CEP fornecido.

## 2. Guia de instalação e configuração
Para utilizar a API, siga os passos abaixo:
1. Instale as dependências necessárias:
```
pip install fastapi uvicorn
```
2. Salve o código da API em um arquivo, por exemplo, `app.py`.
3. Execute a aplicação com o comando:
```
uvicorn app:app --reload
```
4. Acesse a documentação da API em `http://localhost:8000/docs`.

## 3. Descrição detalhada de cada endpoint

### Endpoint: `/endereco/{cep}`
- Método: GET
- Descrição: Consulta um endereço a partir de um CEP fornecido.
- Parâmetros:
  - `cep` (str): CEP a ser consultado.
- Resposta de Sucesso:
  - Código: 200
  - Corpo: Objeto JSON contendo as informações do endereço (logradouro, bairro, cidade, estado).
- Possíveis Respostas de Erro:
  - Código: 404
  - Corpo: Objeto JSON com a mensagem "Endereço não encontrado".

## 4. Exemplos de uso com curl
### Consultar endereço com CEP válido:
```bash
curl -X GET "http://localhost:8000/endereco/12345-678"
```

## 5. Respostas esperadas
### Resposta de Sucesso:
```json
{
  "cep": "12345-678",
  "logradouro": "Rua Exemplo",
  "bairro": "Bairro Teste",
  "cidade": "Cidade Exemplo",
  "estado": "SP"
}
```

### Resposta de Erro (Endereço não encontrado):
```json
{
  "message": "Endereço não encontrado"
}
```

## 6. Códigos de erro possíveis
- 404: Endereço não encontrado