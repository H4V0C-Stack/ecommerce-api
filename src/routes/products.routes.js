const express = require('express');
const router = express.Router();
const productsController = require('../controllers/products.controller');
const authMiddleware = require('../middleware/auth.middleware');

// Публичные маршруты — без токена
router.get('/', productsController.getAll);
router.get('/:id', productsController.getById);

// Защищённые маршруты — нужен JWT токен
router.post('/', authMiddleware, productsController.create);
router.put('/:id', authMiddleware, productsController.update);
router.delete('/:id', authMiddleware, productsController.remove);

module.exports = router;