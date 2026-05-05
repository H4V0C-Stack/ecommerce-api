const jwt = require('jsonwebtoken');

function authMiddleware(req, res, next) {
  // Берём заголовок Authorization: Bearer <token>
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({ error: { status: 401, message: 'Brak tokenu. Zaloguj się.' } });
  }

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded; // сохраняем данные пользователя в запрос
    next();
  } catch (err) {
    return res.status(403).json({ error: { status: 403, message: 'Token nieprawidłowy lub wygasł.' } });
  }
}

module.exports = authMiddleware;