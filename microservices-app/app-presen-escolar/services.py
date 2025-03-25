import flet as ft
from auth import users_db  # Importar o banco de dados de usuários

def show_servicos(page):
    page.clean()
    page.add(ft.Text("Lista de Serviços", size=20))  # Adicionar título

    # Simulação de uma lista de serviços
    services = ["Serviço 1", "Serviço 2", "Serviço 3"]
    for service in services:
        page.add(ft.Text(service, size=16))

    # Exemplo de uso do banco de dados de usuários
    for email in users_db.keys():
        page.add(ft.Text(f"Usuário: {email}", size=16))

    back_button = ft.TextButton("Voltar", on_click=lambda e: show_home(page))  # Botão de voltar
    page.add(back_button)
