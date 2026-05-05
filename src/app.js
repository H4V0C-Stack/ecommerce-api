require('dotenv').config();
const express = require('express');

const authRoutes = require('./routes/auth.routes');
const productRoutes = require('./routes/products.routes');
const orderRoutes = require('./routes/orders.routes');
const errorMiddleware = require('./middleware/error.middleware');

const app = express();

// Говорим Express читать JSON из тела запроса
app.use(express.json());

// Подключаем маршруты
app.use('/auth', authRoutes);
app.use('/products', productRoutes);
app.use('/orders', orderRoutes);

// Глобальная обработка ошибок (всегда последняя)
app.use(errorMiddleware);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Serwer działa na porcie ${PORT}`);
});

module.exports = app;