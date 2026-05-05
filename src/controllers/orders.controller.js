const ordersService = require('../services/orders.service');

function create(req, res, next) {
  try {
    const userId = req.user.id; // берём из JWT токена
    const { items } = req.body;
    const order = ordersService.create(userId, items);
    res.status(201).json(order);
  } catch (err) {
    next(err);
  }
}

function getMyOrders(req, res, next) {
  try {
    const userId = req.user.id;
    const orders = ordersService.getByUser(userId);
    res.status(200).json(orders);
  } catch (err) {
    next(err);
  }
}

module.exports = { create, getMyOrders };