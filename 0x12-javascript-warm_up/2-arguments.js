#!/usr/bin/node

const myArg = process.argv.slice(2);

if (myArg.length === 0) {
  console.log('No Argument');
} else if (myArg.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
