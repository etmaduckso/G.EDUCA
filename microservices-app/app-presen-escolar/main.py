import flet as ft
from login import show_login
from registration import show_registration
from home import show_home
from services import show_servicos
from products import show_produtos
from search import show_pesquisa

def main(page):
    show_login(page)

ft.app(target=main)
