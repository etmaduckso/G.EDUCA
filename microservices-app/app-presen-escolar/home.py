import flet as ft
from auth import users_db  # Importar o banco de dados de usuários
from registration import show_registration  # Importar a função de registro
from login import show_login  # Importar a função de login
from services import show_servicos  # Importar a função de serviços
from products import show_produtos  # Importar a função de produtos
from search import show_pesquisa  # Importar a função de pesquisa

def show_home(name, page):
    page.clean()
    page.add(ft.Text(f"Bem-vindo, {name}!", size=20))
    
    # Adicionando botões para navegar
    servicos_button = ft.ElevatedButton("Serviços", on_click=lambda e: show_servicos(page))
    produtos_button = ft.ElevatedButton("Produtos", on_click=lambda e: show_produtos(page))
    pesquisar_button = ft.ElevatedButton("Pesquisar", on_click=lambda e: show_pesquisa(page))
    
    page.add(servicos_button, produtos_button, pesquisar_button)
    logout_button = ft.ElevatedButton("Sair", on_click=lambda e: show_login(page))  # Adicionar botão de sair
    page.add(logout_button)
