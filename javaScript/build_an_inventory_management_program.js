#!/usr/bin/env node
const inventory = [ {name: 'flour', quantity: 10}, {name: 'rice', qantity: 7} ];
function findProductIndex(productName) {
  productName = productName.toLowerCase();
  for (let i = 0; i < inventory.length; i++) {
    if (productName === inventory[i].name) {
      return i;
    }
  }
  return -1;
}

function addProduct(product) {
  const index = findProductIndex(product.name);
  if (index === -1) {
    product.name = product.name.toLowerCase();
    inventory.push(product);
    console.log(product.name + ' added to inventory');
  } else {
    inventory[index].quantity += product.quantity;
    console.log(product.name.toLowerCase() + ' quantity updated');
  }
}

function removeProduct(productName, quant) {
  const index = findProductIndex(productName);
  if (index === -1) {
    console.log(productName.toLowerCase() + ' not found');
  } else if (inventory[index].quantity >= quant) {
    inventory[index].quantity -= quant;
    console.log(`Remaining ${inventory[index].name} pieces: ${inventory[index].quantity}`);
    if (inventory[index].quantity === 0) {
      inventory.splice(index, 1);
    }
  } else if (inventory[index].quantity < quant ) {
    console.log(`Not enough ${inventory[index].name} available, remaining pieces: ${inventory[index].quantity}`);
  }
}

console.log(inventory);
removeProduct('flour', 10);
console.log(inventory);
