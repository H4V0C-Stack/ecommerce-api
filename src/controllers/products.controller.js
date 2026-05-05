const productsService = require('../services/products.service');

function getAll(req, res, next) {
  try {
    const products = productsService.getAll();
    res.status(200).json(products);
  } catch (err) {
    next(err);
  }
}

function getById(req, res, next) {
  try {
    const id = parseInt(req.params.id);
    if (isNaN(id)) {
      return res.status(400).json({ error: { status: 400, message: 'ID musi być liczbą.' } });
    }
    const product = productsService.getById(id);
    res.status(200).json(product);
  } catch (err) {
    next(err);
  }
}

function create(req, res, next) {
  try {
    const { name, price, category, stock } = req.body;
    const product = productsService.create(name, price, category, stock);
    res.status(201).json(product);
  } catch (err) {
    next(err);
  }
}

function update(req, res, next) {
  try {
    const id = parseInt(req.params.id);
    if (isNaN(id)) {
      return res.status(400).json({ error: { status: 400, message: 'ID musi być liczbą.' } });
    }
    const product = productsService.update(id, req.body);
    res.status(200).json(product);
  } catch (err) {
    next(err);
  }
}

function remove(req, res, next) {
  try {
    const id = parseInt(req.params.id);
    if (isNaN(id)) {
      return res.status(400).json({ error: { status: 400, message: 'ID musi być liczbą.' } });
    }
    const result = productsService.remove(id);
    res.status(200).json(result);
  } catch (err) {
    next(err);
  }
}

module.exports = { getAll, getById, create, update, remove };