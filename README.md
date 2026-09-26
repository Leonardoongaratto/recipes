# Recipes

Site de receitas em Django. Cada receita tem autor, categoria, tempo de preparo, porções, modo de preparo e foto de capa, e só aparece depois de publicada.

## Funcionalidades

- Página inicial com as receitas publicadas, paginadas (tamanho da página configurável por `PER_PAGE`)
- Filtro por categoria e página de detalhe de cada receita
- Busca por texto
- Cadastro de autores com validação de formulário
- Painel administrativo do Django para gerenciar receitas e categorias

## Stack

Python · Django · pytest + pytest-django · Faker · Pillow · Docker

## Testes

A suíte em pytest cobre modelos, views (home, categoria, detalhe, busca), URLs, o formulário de cadastro de autor e a paginação. A cobertura é medida com `coverage`, com branch coverage (`.coveragerc`).

```bash
pytest
coverage run -m pytest && coverage report
```

## Como rodar

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

As variáveis de ambiente estão em `.env-example`: `SECRET_KEY`, `DEBUG` (`1` liga o modo debug) e `PER_PAGE`. Defina-as no shell antes de rodar, por exemplo `export SECRET_KEY=troque-me DEBUG=1`.

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Com Docker:

```bash
docker build -t recipes .
docker run -p 9000:9000 -e SECRET_KEY=troque-me -e DEBUG=1 recipes
```
