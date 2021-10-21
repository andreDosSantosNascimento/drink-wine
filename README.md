# Drink Wine

## Descrição

API desenvolvida para o controle de Produtos, Pedidos, Clientes e Fornecedores, para um distribuidor de vinhos importados. A plataforma utilizada pra fazer o Deploy, foi o Heroku.

## Link da API

[https://drink-wine-api.herokuapp.com/](https://drink-wine-api.herokuapp.com/)

## Requisições

### LOCAL:

#### POST /api/local/country

_Cria um País_

```json
{
  "country_sigla": "BRA",
  "ddd": "+55"
}
```

#### POST /api/local/state

_Cria um Estado_

```json
{
  "state_sigla": "PR",
  "country_sigla": "BRA"
}
```

#### POST /api/local/city

_Cria uma Cidade_

```json
{
  "state_sigla": "PR",
  "ddd": "041"
}
```

### PROVIDER:

#### POST /api/provider

_Cria um Fornecedor_

```json
{
  "name": "ChiWines",
  "email": "contato@chiwines.com",
  "phone": "56612666666",
  "sigla_country": "CHI",
  "nif": "123456789"
}
```

#### PATCH /api/provider/\<id:int>

_Qualquer informação que deseja trocar sobre o Fornecedor pode ser passada, sendo ao menos uma das opções apresentadas no POST_

```json
{
  "phone": "56612777777"
}
```

#### DELETE /api/provider/\<id:int>

_Quando você faz o delete não precisa do corpo da requisição com informações, apenas o ID do Fornecedor que deseja retirar_

#### GET /api/provider

_Retorna a lista de Fornecedores cadastrados, não precisa de corpo e tem o seguinte retorno_

```json
{
  "data": [
    {
      "name": "ChiWines",
      "email": "contato@chiwines.com",
      "phone": "56612666666",
      "sigla_country": "CHI",
      "nif": "123456789"
    },
    {
      "name": "ArgWines",
      "email": "contato@argwines.com",
      "phone": "56612878787",
      "sigla_country": "ARG",
      "nif": "234567891"
    }
  ]
}
```

### CLIENT:

#### POST /api/client

_Cria um Cliente_

```json
{
  "name": "Pizzaria Verde",
  "email": "contato@pizzaverde.com",
  "phone": "5541999999999",
  "ddd_city": "041",
  "cnpj": "00111222000133"
}
```

#### PATCH /api/client/\<id:int>

_Qualquer informação que deseja trocar sobre o Cliente pode ser passada, sendo ao menos uma das opções apresentadas no POST_

```json
{
  "phone": "5541988888888"
}
```

#### DELETE /api/client/\<id:int>

_Quando você faz o delete não precisa do corpo da requisição com informações, apenas o ID do Cliente que deseja retirar_

#### GET /api/client

_Retorna a lista de Clientes cadastrados, não precisa de corpo e tem o seguinte retorno_

```json
{
  "data": [
    {
      "name": "Pizzaria Verde",
      "email": "contato@pizzaverde.com",
      "phone": "5541999999999",
      "ddd_city": "041",
      "cnpj": "00111222000133"
    },
    {
      "name": "Pizzaria Azul",
      "email": "contato@pizzaazul.com",
      "phone": "5541988888888",
      "ddd_city": "041",
      "cnpj": "00111222000144"
    }
  ]
}
```

#### GET /api/client/\<id:int>

_Retorna o Cliente cadastrado, não precisa de corpo e tem o seguinte retorno_

```json
{
  "data": [
    {
      "name": "Pizzaria Verde",
      "email": "contato@pizzaverde.com",
      "phone": "5541999999999",
      "ddd_city": "041",
      "cnpj": "00111222000133"
    }
  ]
}
```

### ORDERS:

#### POST /api/orders

_Cria um Pedido_

```json
{
  "client_email": "contato@pizzaverde.com",
  "provider_email": "contato@chiwines.com",
  "products": ["Vinho Branco", "Vinho Vermelho", "Vinho da Serra", "Vinho Azul"]
}
```

#### PATCH /api/orders/\<id:int>

_Informação que deseja trocar sobre o Pedido pode ser passada, sendo ao menos uma das opções apresentadas no POST exceto produtos_

```json
{
  "provider_email": "arg_wines@mail.com"
}
```

#### DELETE /api/orders/\<id:int>

_Quando você faz o delete não precisa do corpo da requisição com informações, apenas o ID do Pedido que deseja retirar_

### PRODUCTS:

#### POST /api/product

_Cria um Produto_

```json
{
  "name": "Vinho Cinza",
  "value": 550.5,
  "description": "Vinho do Chile Merlot",
  "expiration_date": "23/02/2029"
}
```

#### PATCH /api/product/\<id:int>

_Informação que deseja trocar sobre o Produto pode ser passada, sendo ao menos uma das opções apresentadas no POST_

```json
{
  "value": 455.5
}
```

#### DELETE /api/product/\<id:int>

_Quando você faz o delete não precisa do corpo da requisição com informações, apenas o ID do Produto que deseja retirar_

#### GET /api/product

_Retorna todos os produtos cadastrados, não precisa de corpo e tem o seguinte retorno_

```json
{
  "data": [
    {
      "name": "Vinho Cinza",
      "value": 550.5,
      "description": "Vinho do Chile Merlot",
      "expiration_date": "2029/09/20"
    },
    {
      "name": "Vinho Bege",
      "value": 1000,
      "description": "Vinho da Argentina Merlot",
      "expiration_date": "23/02/2029"
    },
    {
      "name": "Vinho Celeste",
      "value": 30.99,
      "description": "Vinho do Argentino Cabernet Sauvignon",
      "expiration_date": "23/02/2029"
    }
  ]
}
```

## Equipe

Projeto implementado por:

[André Nascimento](https://www.linkedin.com/in/andre-nascimento-b543831a9/) **_P.O._**

[Guilherme Gonçalves](https://www.linkedin.com/in/guilhermecosgoncalves/) **_T.L._**

[Charles Pinheiro](https://www.linkedin.com/in/charles-pinheiro-052356205/) **_S.M._**

[Rodrigo Ferraz](https://www.linkedin.com/in/how-dev-rodrigo/) **_DEV_**

[Eduardo Godoi](https://www.linkedin.com/in/eduardo-godoi-12263b122/) **_DEV_**

Todos além de desenvolverem o código executaram as funções que estão ao lado do nome, como forma de agregar conhecimento sobre as funções de um projeto.
