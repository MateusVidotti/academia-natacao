# Sistema para gestão de academia de natação

### Para executar com docker
- Necessário o docker no ambiente
- Clone o diretório
- Acesse o diretório e execute`docker-compose up --build`
- URL admin do django: http://localhost:8000/admin (user: admin, password: admin)
- URL app web: http://localhost:8080/
- No arquivo `.env` estão as variáveis de ambiente

#### Serviços utilizados
- banco de dados: PostgreSQL
- backend: django

### Para executar em um ambiente virtual
- criar um ambiente virtual python.
- acesse a pasta do projeto
- acesse a pasta swimming_gym `cd swimming_gym`
- execute `pip install requirements.txt` para instalar as dependências.
- Na primeira execução, faça a migração do db executando `python manage.py makemigrations` e `python manage.py migrate`
- Na primeira execução, crie um usuário admin executando `python manage.py createsuperuser` entre com email e senha.
- para executar o servidor django `python manage.py runserver`



