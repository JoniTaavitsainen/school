'use strict';

document.querySelector('#source').addEventListener('submit', (event) => {
  event.preventDefault();
  const firstName = document.querySelector('input[name="firstname"]').value;
  const lastName = document.querySelector('input[name="lastname"]').value;
  document.querySelector('#target').textContent = `Your name is ${firstName} ${lastName}`;
});