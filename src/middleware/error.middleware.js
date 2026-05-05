function errorMiddleware(err, req, res, next) {
  const status = err.status || 500;
  const message = err.message || 'Wewnętrzny błąd serwera';

  res.status(status).json({
    error: {
      status,
      message
    }
  });
}

module.exports = errorMiddleware;