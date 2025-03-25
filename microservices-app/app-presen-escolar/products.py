import flet as ft
from auth import users_db  # Importar o banco de dados de usuários

def show_produtos(page):
    page.clean()
    page.add(ft.Text("Lista de Produtos", size=20))  # Adicionar título

    # Simulação de uma lista de produtos
    products = ["Produto 1", "Produto 2", "Produto 3"]
    for product in products:
        page.add(ft.Text(product, size=16))

    # Exemplo de uso do banco de dados de usuários
    for email in users_db.keys():
        page.add(ft.Text(f"Usuário: {email}", size=16))

    back_button = ft.TextButton("Voltar", on_click=lambda e: show_home(page))  # Botão de voltar
    page.add(back_button)
