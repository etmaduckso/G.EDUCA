document.getElementById('register-button').addEventListener('click', async () => {
    const name = document.getElementById('name').value;
    const username = document.getElementById('register-username').value;
    const password = document.getElementById('register-password').value;

    // Verifica se o usuário já está cadastrado
    const existingUsers = JSON.parse(sessionStorage.getItem('users')) || [];
    const userExists = existingUsers.some(user => user.username === username);
    if (userExists) {
        alert('Usuário já cadastrado. Tente fazer login.');
        return;
    }

    // Salva os dados de cadastro no sessionStorage
    existingUsers.push({ name, username, password });
    sessionStorage.setItem('users', JSON.stringify(existingUsers));

    const response = await fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, username, password }),
    });

    const message = await response.text();
    alert(message);

    // Redireciona para a página index.html apenas se o cadastro for bem-sucedido
    if (response.ok) {
        window.location.href = 'index.html';
    } else {
        alert('Erro ao cadastrar. Tente novamente.');
    }
});

document.getElementById('login-button').addEventListener('click', async () => {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Verifica se os campos estão preenchidos
    if (!username || !password) {
        alert('Por favor, preencha todos os campos.');
        return;
    }

    // Validação de senha
    if (password.length < 8) {
        alert('A senha deve ter pelo menos 8 caracteres.');
        return;
    }

    // Verifica se os dados estão no sessionStorage
    const existingUsers = JSON.parse(sessionStorage.getItem('users')) || [];
    const user = existingUsers.find(user => user.username === username && user.password === password);

    if (user) {
        // Redireciona para a página home apenas se o login for bem-sucedido
        window.location.href = 'home.html';
    } else {
        alert('Credenciais inválidas. Tente novamente.');
    }
});
