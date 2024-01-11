# Projeto Web Curso de Férias
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

---

<div style="text-align: center;">
  <img src="https://upload.wikimedia.org/wikipedia/pt/7/74/Logo_Unijorge.jpg" alt="Texto Alternativo" style="width: 25%;">
</div>


## Importante:

>"Lembre-se de renomear o arquivo *.env-example* para *.env e alterar* os valores das variáveis de ambiente."

```
SECRET_KEY='Change-me'
ALLOWED_HOSTS='Change-me'
ENGINE='Change-me'
NAME='Change-me'
USER='Change-me'
PASSWORD='Change-me'
HOST='Change-me'
PORT='Change-me'

```

## Comandos úteis:

*Criar ambiente virtual* 
`python -m venv .venv`

*Ativar ambiente virtual* 
`.\.venv\Scripts\activate`

*Instalar dependências* 
`pip install -r requirements.txt`

*Autualizar o arquivo requirements.txt* 
`pip freeze > requirements.txt`

*Iniciar servidor* 
`python manage.py runserver`

*Fazer Migrations* 
`python manage.py makemigrations`

*Migar para banco de dados* 
`python manage.py migrate`

*Criar superusuário* 
`python manage.py createsuperuser`



