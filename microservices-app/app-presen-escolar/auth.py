import hashlib

# Simulação de um banco de dados de usuários
users_db = {}

def register_user(name, email, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users_db[email] = {'name': name, 'password': hashed_password}
    print(f"Usuário cadastrado: {name}, {email}.")

def login_user(email, password):
    user = users_db.get(email)
    if user and user['password'] == hashlib.sha256(password.encode()).hexdigest():
        return user['name']
    return None
