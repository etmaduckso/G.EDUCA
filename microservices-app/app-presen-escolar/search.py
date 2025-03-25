import flet as ft
from auth import users_db  # Importar o banco de dados de usuários
# Remover a importação circular


def show_pesquisa(page):
    page.clean()
    page.add(ft.Text("Pesquisa", size=20))  # Adicionar título
    search_input = ft.TextField(label="Digite sua pesquisa")
    search_button = ft.ElevatedButton("Pesquisar", on_click=lambda e: perform_search(search_input.value, page))
    back_button = ft.TextButton("Voltar", on_click=lambda e: show_home(page))  # Botão de voltar
    page.add(back_button)

    page.add(search_input, search_button, back_button)

def perform_search(query, page):
    # Simulação de resultados de pesquisa
    results = [f"Resultado para '{query}'" for _ in range(3)]
    for result in results:
        page.add(ft.Text(result, size=16))

    # Exemplo de uso do banco de dados de usuários
    for email in users_db.keys():
        page.add(ft.Text(f"Usuário: {email}", size=16))
