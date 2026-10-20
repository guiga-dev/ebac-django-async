# Concorr�ncia Django

Projeto independente com view `async def`, `await asyncio.sleep` e execu��o concorrente via `asyncio.gather`. A cada acesso a `/async/`, o terminal exibe explicitamente `Contador: 1` at� `Contador: 10`, reiniciando a contagem na pr�xima requisi��o.

Instale `requirements.txt`, rode `python manage.py runserver`, acesse `/async/` e observe os c�lculos no terminal.
Testes: `python manage.py test`.
Entregar novo reposit�rio e PR (`codex/async-view` contra `main`).
