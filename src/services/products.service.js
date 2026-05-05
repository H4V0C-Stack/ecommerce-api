// База продуктов в памяти
const products = [
  { id: 1, name: 'Laptop Dell XPS 15', price: 5999.99, category: 'laptopy', stock: 10 },
  { id: 2, name: 'iPhone 15 Pro', price: 4999.99, category: 'telefony', stock: 25 },
  { id: 3, name: 'Sony WH-1000XM5', price: 1299.99, category: 'sluchawki', stock: 50 }
];

let nextId = 4;

function getAll() {
  return products;
}

function getById(id) {
  const product = products.find(p => p.id === id);
  if (!product) {
    const err = new Error('Produkt nie został znaleziony.');
    err.status = 404;
    throw err;
  }
  return product;
}

function create(name, price, category, stock) {
  if (!name || !price || !category) {
    const err = new Error('Nazwa, cena i kategoria są wymagane.');
    err.status = 400;
    throw err;
  }
  if (price <= 0) {
    const err = new Error('Cena musi być większa niż 0.');
    err.status = 400;
    throw err;
  }

  const newProduct = {
    id: nextId++,
    name,
    price: parseFloat(price),
    category,
    stock: stock || 0
  };
  products.push(newProduct);
  return newProduct;
}

function update(id, data) {
  const product = getById(id);

  if (data.price !== undefined && data.price <= 0) {
    const err = new Error('Cena musi być większa niż 0.');
    err.status = 400;
    throw err;
  }

  if (data.name !== undefined) product.name = data.name;
  if (data.price !== undefined) product.price = parseFloat(data.price);
  if (data.category !== undefined) product.category = data.category;
  if (data.stock !== undefined) product.stock = data.stock;

  return product;
}

function remove(id) {
  const index = products.findIndex(p => p.id === id);
  if (index === -1) {
    const err = new Error('Produkt nie został znaleziony.');
    err.status = 404;
    throw err;
  }
  products.splice(index, 1);
  return { message: 'Produkt został usunięty.' };
}

module.exports = { getAll, getById, create, update, remove };