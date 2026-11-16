'use strict';

document.querySelector('#start').addEventListener('click', () => {
  const firstInput = document.querySelector('#num1').value.trim();
  const secondInput = document.querySelector('#num2').value.trim();
  const result = document.querySelector('#result');
  const first = Number(firstInput);
  const second = Number(secondInput);

  if (!firstInput || !secondInput || !Number.isFinite(first) || !Number.isFinite(second)) {
    result.textContent = 'Please enter two valid numbers.';
    return;
  }

  switch (document.querySelector('#operation').value) {
    case 'add':
      result.textContent = first + second;
      break;
    case 'sub':
      result.textContent = first - second;
      break;
    case 'multi':
      result.textContent = first * second;
      break;
    case 'div':
      result.textContent = second === 0 ? 'Cannot divide by zero.' : first / second;
      break;
    default:
      result.textContent = 'Please select a valid operation.';
  }
});