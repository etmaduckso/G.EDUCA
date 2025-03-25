import flet as ft
from auth import login_user  # Importar a função de login
from registration import show_registration  # Importar a função de registro

def show_login(page):
    page.clean()
    page.add(ft.Text("Login", size=20))
    email_input = ft.TextField(label="E-mail")
    password_input = ft.TextField(label="Senha", password=True)
    login_button = ft.ElevatedButton("Entrar", on_click=lambda e: handle_login(email_input.value, password_input.value, page))
    register_link = ft.TextButton("Cadastrar", on_click=lambda e: show_registration(page))
    page.add(email_input, password_input, login_button, register_link)

def handle_login(email, password, page):
    name = login_user(email, password)
    if name:
        from home import show_home  # Importar a função de home aqui para evitar circularidade
        show_home(name, page)
    else:
        page.add(ft.Text("Login inválido. Tente novamente ou cadastre-se.", color=ft.colors.RED))
