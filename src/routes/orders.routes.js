const express = require('express');
const router = express.Router();
const ordersController = require('../controllers/orders.controller');
const authMiddleware = require('../middleware/auth.middleware');

// Все маршруты заказов защищены
router.post('/', authMiddleware, ordersController.create);
router.get('/', authMiddleware, ordersController.getMyOrders);

module.exports = router;