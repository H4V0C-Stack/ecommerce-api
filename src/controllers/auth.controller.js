const authService = require('../services/auth.service');

function register(req, res, next) {
  try {
    const { email, password } = req.body;

    // Валидация входных данных
    if (!email || !password) {
      return res.status(400).json({ error: { status: 400, message: 'Email i hasło są wymagane.' } });
    }
    if (password.length < 6) {
      return res.status(400).json({ error: { status: 400, message: 'Hasło musi mieć minimum 6 znaków.' } });
    }

    const result = authService.register(email, password);
    res.status(201).json({ message: 'Rejestracja udana.', user: result });
  } catch (err) {
    next(err); // передаём ошибку в error middleware
  }
}

function login(req, res, next) {
  try {
    const { email, password } = req.body;

    if (!email || !password) {
      return res.status(400).json({ error: { status: 400, message: 'Email i hasło są wymagane.' } });
    }

    const result = authService.login(email, password);
    res.status(200).json(result);
  } catch (err) {
    next(err);
  }
}

module.exports = { register, login };