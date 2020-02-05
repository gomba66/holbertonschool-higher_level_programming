#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  let i = 2;
  let x = process.argv[2];
  let y = x;
  while (i < process.argv.length) {
    y = x;
    if (parseInt(process.argv[i]) > x) {
      x = parseInt(process.argv[i]);
    }
    i++;
  }
  console.log(y);
}
