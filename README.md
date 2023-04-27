
 - Python3.11
 - Poetry == 1.2.2
 - Django == 4.2
 - PostgreSQL
 - pgadmin
 - Dockerfile
 - Docker-compose

Após clonar o projeto, inicializar seu ambiente virtual,
digitar o comando 
    <docker compose build>
em seguida o comando
    <docker compose up>
após gerar as imagens e inicializar os 03 containers, será necessário
sincronizar o IP do container <postgres>.
em settings do projeto, irá alterar o host do bd para o atual
container. 
Para identificar o IP do container, digitar o comando:
    <docker container ls>
serão listados os 03 containers que estão ativos, vamos precisar do
ID do container que contenha o <postgres>
Com o ID, no terminal basta digitar:
    <docker inspect <id do container> | grep "IPAddress>
agora, basta inserir este IP no host do banco de dados, em seguida
digitar o comando
    <docker compose restart>

O projeto estará em localhost:8000/

O pgadmin estará em localhost:5050
    login e senha para acesso ao pgadmin:
        login = admin@admin.com
        senha = admin
    ao acessar o pgadmin, a senha de conexão:
        login = postgres


01 Pessoa pode ter até 03 carros
    Tabela 1 -> N
    Se a pessoa que tem 03 carros tentar comprar outro carro, receber
    mensagem na tela que já possui numero máximo de carros permitido.

Carros
Criar categorias:
    Cores: Amarelo
            Azul
            Cinza

    Modelo: Hatch
            Sedã
            Conversivel

Não pode existir carros cadastrados sem proprietários

Pode cadastrar pessoas que ainda não tenham carros, e estes, precisam ser
    identificados como: Oporttunidade de vendas

Quando uma pessoa em oportunidade de vendas adquirir um veículo, 
automaticamente ela é removida da lista de oportunidade de vendas.
