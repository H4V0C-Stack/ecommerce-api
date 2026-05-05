const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

// База пользователей в памяти (без настоящей БД)
const users = [];

function register(email, password) {
  // Проверяем что такой email ещё не занят
  const existing = users.find(u => u.email === email);
  if (existing) {
    const err = new Error('Użytkownik z tym emailem już istnieje.');
    err.status = 409;
    throw err;
  }

  // Хешируем пароль
  const hashedPassword = bcrypt.hashSync(password, 10);
  const newUser = {
    id: users.length + 1,
    email,
    password: hashedPassword
  };
  users.push(newUser);

  return { id: newUser.id, email: newUser.email };
}

function login(email, password) {
  const user = users.find(u => u.email === email);
  if (!user) {
    const err = new Error('Nieprawidłowy email lub hasło.');
    err.status = 401;
    throw err;
  }

  const isValid = bcrypt.compareSync(password, user.password);
  if (!isValid) {
    const err = new Error('Nieprawidłowy email lub hasło.');
    err.status = 401;
    throw err;
  }

  // Создаём JWT токен — действует 24 часа
  const token = jwt.sign(
    { id: user.id, email: user.email },
    process.env.JWT_SECRET,
    { expiresIn: '24h' }
  );

  return { token };
}

module.exports = { register, login };