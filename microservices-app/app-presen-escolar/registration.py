import hashlib
import flet as ft
from auth import register_user  # Importar a função de registro

def show_registration(page):
    page.clean()
    page.add(ft.Text("Cadastro de Usuário", size=20))

    name_input = ft.TextField(label="Nome")
    email_input = ft.TextField(label="E-mail")
    password_input = ft.TextField(label="Senha", password=True)
    register_button = ft.ElevatedButton("Cadastrar", on_click=lambda e: handle_registration(name_input.value, email_input.value, password_input.value, page))
    page.add(name_input, email_input, password_input, register_button)

def handle_registration(name, email, password, page):
    register_user(name, email, password)
    from login import show_login  # Importar a função de login
    from login import show_login  # Importar a função de login
    show_login(page)  # Chamar a função de login após o registro
