#!/usr/bin/node

const Error = 'Missing number of occurrences';

const num = Math.floor(+process.argv[2]);

if (isNaN(num)) {
  console.log(Error);
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
