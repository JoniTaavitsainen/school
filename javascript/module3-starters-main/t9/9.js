'use strict';

document.querySelector('#start').addEventListener('click', () => {
  const input = document.querySelector('#calculation').value;
  const result = document.querySelector('#result');
  const match = input.match(/^\s*([+-]?\d+)\s*([+\-*/])\s*([+-]?\d+)\s*$/);

  if (!match) {
    result.textContent = 'Please enter a calculation with two integers.';
    return;
  }

  const first = Number(match[1]);
  const second = Number(match[3]);
  switch (match[2]) {
    case '+':
      result.textContent = first + second;
      break;
    case '-':
      result.textContent = first - second;
      break;
    case '*':
      result.textContent = first * second;
      break;
    case '/':
      result.textContent = second === 0 ? 'Cannot divide by zero.' : first / second;
      break;
  }
});