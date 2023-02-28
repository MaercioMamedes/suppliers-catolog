# Projeto Suppliers Catolog

Essa aplicação é um classificados de fornecedores para festas e eventos. Nele o usuário fornecedor irá cadastrar seus serviços
oferecidos, estipular preços, e agendar o atendimento no evento. Equanto o cliente irá pesquisar os serviços de seu interesse
entrar em contato com o fornecedor agendar a data da execução do serviço
### Como rodar ?

* realize o clone do repositório - `git clone https://github.com/MaercioMamedes/suppliers-catolog.git`
* [crie um ambiente virtual dentro do diretório do projeto e instale todas as dependências](https://www.alura.com.br/artigos/ambientes-virtuais-em-python)
* rode o comando `python manage.py runserver`


### Usuários e senhas para ambiente de testes

| username  | password |   type    |
|:---------:|:--------:|:---------:|
|  maercio  | csa2325  | superuser |
|  york01   |   2325   | supplier  |
| gourmet01 |   2325   | supplier  |
|  nath02   |   2325   |  client   |

### Etapas do projeto

* :heavy_check_mark: Criar modelos e definir relacionamentos
* :heavy_check_mark:: template base do projeto
* :heavy_check_mark: view e rota para index
* :heavy_check_mark: view e rota de cadastro de cliente
* :heavy_check_mark: view e rota de cadastro de fornecedor
* :heavy_check_mark: view e rota de autenticação de usuário
* :heavy_check_mark: rota para logout
* :heavy_check_mark: view e rota de autalização de usuário
* :x: view e rota de exclusão de usuário
* :heavy_check_mark: view e rota de cadastro de serviço
* :heavy_check_mark: view e rota de atualização de serviço
* :x: view e rota da agenda do fornecedor
* :x: view e rota para comentários e nota do serviço
* :x: view e rota para dashboard de usuário fornecedor
* :x: view e rota para dashboard de usuário cliente
* :x: view e rota para dashboard de usuário administrador
* :x: validação de formulários
* :x: mensagens de confirmações e erros
* :x: requisições assícronas com javascript
* :x: deploy
