#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Missing number of ocurrences');
} else {
  let i = 0;
  const number = parseInt(process.argv[2]);
  while (i < number) {
    console.log('C is fun');
    i++;
  }
}
