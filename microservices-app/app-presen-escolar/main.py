import flet as ft

# Simulação de um banco de dados de usuários
users_db = {}

def main(page: ft.Page):
    page.title = "Aplicação de Login e Cadastro"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Função para exibir a tela de cadastro
    def show_registration():
        page.clean()
        page.add(ft.Text("Cadastro de Usuário", size=20))
        name_input = ft.TextField(label="Nome")
        email_input = ft.TextField(label="E-mail")
        password_input = ft.TextField(label="Senha", password=True)
        register_button = ft.ElevatedButton("Cadastrar", on_click=lambda e: register_user(name_input.value, email_input.value, password_input.value))
        page.add(name_input, email_input, password_input, register_button)

    # Função para registrar o usuário
    def register_user(name, email, password):
        users_db[email] = {'name': name, 'password': password}
        print(f"Usuário cadastrado: {name}, {email}")
        show_login()

    # Função para exibir a tela de login
    def show_login():
        page.clean()
        page.add(ft.Text("Login", size=20))
        email_input = ft.TextField(label="E-mail")
        password_input = ft.TextField(label="Senha", password=True)
        login_button = ft.ElevatedButton("Entrar", on_click=lambda e: login_user(email_input.value, password_input.value))
        register_link = ft.TextButton("Cadastrar", on_click=lambda e: show_registration())
        page.add(email_input, password_input, login_button, register_link)

    # Função para fazer login
    def login_user(email, password):
        user = users_db.get(email)
        if user and user['password'] == password:
            show_home(user['name'])
        else:
            page.add(ft.Text("Login inválido. Tente novamente ou cadastre-se.", color=ft.colors.RED))

    # Função para exibir a página home
    def show_home(name):
        page.clean()
        page.add(ft.Text(f"Bem-vindo, {name}!", size=20))
        
        # Adicionando botões para navegar
        servicos_button = ft.ElevatedButton("Serviços", on_click=lambda e: show_servicos())
        produtos_button = ft.ElevatedButton("Produtos", on_click=lambda e: show_produtos())
        pesquisar_button = ft.ElevatedButton("Pesquisar", on_click=lambda e: show_pesquisa())
        
        page.add(servicos_button, produtos_button, pesquisar_button)
        logout_button = ft.ElevatedButton("Sair", on_click=lambda e: show_login())
        page.add(logout_button)

    def show_servicos():
        # Lógica para exibir serviços
        pass

    def show_produtos():
        # Lógica para exibir produtos
        pass

    def show_pesquisa():
        # Lógica para pesquisa
        pass

    # Exibir a tela de login inicialmente
    show_login()

ft.app(target=main)
