#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('Missing size');
} else {
  let x = 0;
  let y = 0;
  const character = 'X';
  let characters = '';
  const number = parseInt(process.argv[2]);

  while (x < number) {
    characters = characters + character;
    x++;
  }
  while (y < number) {
    console.log(characters);
    y++;
  }
}
