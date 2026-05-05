const productsService = require('./products.service');

// База заказов в памяти
const orders = [];
let nextId = 1;

function create(userId, items) {
  if (!items || !Array.isArray(items) || items.length === 0) {
    const err = new Error('Zamówienie musi zawierać przynajmniej jeden produkt.');
    err.status = 400;
    throw err;
  }

  // Sprawdzamy każdy produkt i liczymy cenę
  let totalPrice = 0;
  const orderItems = items.map(item => {
    if (!item.productId || !item.quantity || item.quantity <= 0) {
      const err = new Error('Każdy produkt musi mieć productId i quantity większe niż 0.');
      err.status = 400;
      throw err;
    }

    const product = productsService.getById(item.productId);
    const subtotal = product.price * item.quantity;
    totalPrice += subtotal;

    return {
      productId: product.id,
      name: product.name,
      price: product.price,
      quantity: item.quantity,
      subtotal: parseFloat(subtotal.toFixed(2))
    };
  });

  const newOrder = {
    id: nextId++,
    userId,
    items: orderItems,
    totalPrice: parseFloat(totalPrice.toFixed(2)),
    status: 'nowe',
    createdAt: new Date().toISOString()
  };

  orders.push(newOrder);
  return newOrder;
}

function getByUser(userId) {
  return orders.filter(o => o.userId === userId);
}

module.exports = { create, getByUser };