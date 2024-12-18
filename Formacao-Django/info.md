# [Formação Django Alura](https://cursos.alura.com.br/formacao-django)

## Inicializando com django

### Inicializando projeto

```bash
$django-admin startproject NOME-PROJETO
```

Com isso ele criará

- **manage.py**: script para gerenciar a aplicação Django.
- **_init_py**: arquivo vazio que indica um package.
- **settings.py**: arquivo de configuração do projeto.
- **urls.py**: todas as urls do projeto são definidas aqui.
- **wsgi.py**: protocolo que serve http.

### Criando banco de dados

O comendo abaixo pode ser usado para rodar todas as migrations e também para criar o banco de dados

```bash
$python manage.py migrate
```

## Rodando o projeto

```bash
$python manage.py runserver
```

## Inicializando app

```bash
$python manage.py startapp nome_do_app
```

### Criando um super user

```bash
$python manage.py createsuperuser
```

### Lidando com arquivos estáticos

```bash
$python manage.py collectstatic
```
