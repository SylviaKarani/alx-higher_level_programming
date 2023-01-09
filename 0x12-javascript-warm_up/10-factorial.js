#!/usr/bin/node

function fact (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }
  return num * fact(num - 1);
}

const num = +process.argv[2];

const res = fact(num);

console.log(res);
