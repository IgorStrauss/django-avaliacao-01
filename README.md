
# Projeto administrando quantidade de veículos por pessoa: Django + Djangorestfremework


 - Python3.11
 - Poetry == 1.2.2
 - Django == 4.2
 - Djangorestframework
 - PostgreSQL
 - pgadmin
 - Dockerfile
 - Docker-compose

## Clonando o projeto
Após clonar o projeto, inicializar seu ambiente virtual, em seguida:
digitar o comando 
###    docker compose build
em seguida o comando
###    docker compose up

Os 03 containers estão com IPs definidos no docker-compose e no DB do settings.

O projeto estará em localhost:8000/

Rotas do projeto:
 - LOCALHOST:8000 → Página inicial
 - LOCALHOST:8000/persons/ → Listar todas pessoas cadastradas
 - LOCALHOST:8000/oportunity/ → Listar pessoas cadastradas que não possuem veículo
 - LOCALHOST:8000/owner/ → Listar pessoas que possuem veículo(s)
 - LOCALHOST:8000/register-car/ → Área para cadastro de veículo
 - LOCALHOST:8000/create-person/ → Área para cadastro de pessoa
 - LOCALHOST:8000/<int:person_id>/ → Profile de pessoa que não possui veículo
 - LOCALHOST:8000/persons-cars/<int:person_id>/ → Profile de pessoa que possui veículo e lista com veículo(s) cadastrado(s)
 - LOCALHOST:8000/update/<int:person_id>/ → Área para atualizar dados da pessoa
 - LOCALHOST:8000/delete-car/<int:car_id>/ → Área para deletar carro por Car_ID
 - LOCALHOST:8000/search/?termo= → Pesquisa de pessoa exclusivamente por CPF

Rotas API:
 - GET    localhost:8000/api/v1/persons/ → Listar todas pessoas cadastradas
 - GET    localhost:8000/api/v1/persons/person_id/ → Listar dados person_id
 - POST   localhost:8000/api/v1/persons/create/ → Cadastrar pessoa
 - PATCH  localhost:8000/api/v1/persons/<int:person_id>/update/ → Atualizar dados de pessoa person_id
 - GET    localhost:8000/api/v1/cars/ → Listar todos veículos cadastrados
 - GET    localhost:8000/api/v1/cars/<int:car_id>/ → Listar veículo por car_id
 - POST   localhost:8000/api/v1/cars/create/ → Cadastrar veículo
 - PATCH  localhost:8000/api/v1/cars/<int:car_id>/ → Atualizar dados veículo por car_id
 - DELETE localhost:8000/api/v1/cars/<int:car_id>/ → Deletar veículo por car_id
 - GET    localhost:8000/api/v1/persons/owner/false/ → Listar pessoas que não possuem veículo
 - GET    localhost:8000/api/v1/persons/owner/true/ → Listar pessoas que possuem veículo
 - GET    localhost:8000/api/v1/person_car/<int:person_id>/ → Listar dados de person_id e todos os veículos associados a ela

O pgadmin estará em localhost:5050

    login e senha para acesso ao pgadmin:
        login = admin@admin.com
        senha = admin

    Ao acessar o pgadmin, a senha de conexão:
        login = postgres


01 Pessoa pode ter até 03 veículos

Tabela 1 -> N
Se a pessoa que tem 03 veículos tentar comprar outro veículo, receber
mensagem na tela que já possui numero máximo de veículos permitido.

### Carros

Criar categorias:

    Cores: Amarelo
            Azul
            Cinza

    Modelo: Hatch
            Sedã
            Conversivel

Não pode existir carros cadastrados sem proprietários

Pode cadastrar pessoas que ainda não tenham carros, e estes, precisam ser
identificados como: Oportunidade de vendas

Quando uma pessoa em oportunidade de vendas adquirir um veículo, 
automaticamente ela é removida da lista de oportunidade de vendas.
