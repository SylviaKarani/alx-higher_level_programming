#!/usr/bin/node

const num = +process.argv[2];

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number:', Math.floor(num));
}
