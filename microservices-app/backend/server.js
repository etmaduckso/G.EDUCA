const express = require('express');
const app = express();
const bodyParser = require('body-parser');

app.use(bodyParser.json());

const users = []; // In-memory user storage

app.post('/register', (req, res) => {
    const { username, password } = req.body;
    // Check if user already exists
    const existingUser = users.find(user => user.username === username);
    if (existingUser) {
        return res.status(400).send('User already exists');
    }
    // Add new user
    users.push({ username, password });
    res.send('User registered');
});


app.post('/login', (req, res) => {
    const { username, password } = req.body;
    // Find user
    const user = users.find(user => user.username === username);
    if (!user || user.password !== password) {
        return res.status(401).send('Invalid credentials');
    }
    res.send('User logged in');
});


const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
