#!/usr/bin/node

let quantity = 0;

const logMe = (item) => {
  console.log(`${quantity}: ${item}`);
  quantity++;
};

module.exports = { logMe };
