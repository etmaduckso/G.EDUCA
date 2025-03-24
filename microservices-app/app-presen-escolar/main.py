import flet as ft

# Simulação de um banco de dados de usuários
users_db = {}

def main(page: ft.Page):
    page.title = "Aplicação de Login e Cadastro"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Função para exibir a tela de cadastro de escolas
    def show_registration():
        page.clean()
        page.add(ft.Text("Cadastro de Escola", size=20))

        name_input = ft.TextField(label="Nome")
        email_input = ft.TextField(label="E-mail")
        password_input = ft.TextField(label="Senha", password=True)
        register_button = ft.ElevatedButton("Cadastrar", on_click=lambda e: register_user(name_input.value, email_input.value, password_input.value))
        page.add(name_input, email_input, password_input, register_button)

    # Função para registrar o usuário com senha hash
    def register_user(name, email, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        users_db[email] = {'name': name, 'password': hashed_password}

        print(f"Usuário cadastrado: {name}, {email}.")
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
        if user and user['password'] == hashlib.sha256(password.encode()).hexdigest():

            show_home(user['name'])
        else:
            page.add(ft.Text("Login inválido. Tente novamente ou cadastre-se.", color=ft.colors.RED))

    # Função para exibir a página home com controle de acesso
    def show_home(name):
        if name == "admin":
            page.clean()
            page.add(ft.Text(f"Bem-vindo, {name}! Você tem acesso total.", size=20))
        else:
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
        page.clean()
        page.add(ft.Text("Lista de Serviços", size=20))

        # Simulação de uma lista de serviços
        services = ["Serviço 1", "Serviço 2", "Serviço 3"]
        for service in services:
            page.add(ft.Text(service, size=16))

    def show_produtos():
        page.clean()
        page.add(ft.Text("Lista de Produtos", size=20))

        # Simulação de uma lista de produtos
        products = ["Produto 1", "Produto 2", "Produto 3"]
        for product in products:
            page.add(ft.Text(product, size=16))

    def show_pesquisa():
        page.clean()
        page.add(ft.Text("Pesquisa", size=20))
        search_input = ft.TextField(label="Digite sua pesquisa")
        search_button = ft.ElevatedButton("Pesquisar", on_click=lambda e: perform_search(search_input.value))
        page.add(search_input, search_button)

    def perform_search(query):
        # Simulação de resultados de pesquisa
        results = [f"Resultado para '{query}'" for _ in range(3)]
        for result in results:
            page.add(ft.Text(result, size=16))

    # Exibir a tela de login inicialmente
    show_login()

ft.app(target=main)
