'use strict';

const target = document.querySelector('#target');
const items = ['First item', 'Second item', 'Third item'];

for (let i = 0; i < items.length; i++) {
  const item = document.createElement('li');
  item.textContent = items[i];
  if (i === 1) {
    item.classList.add('my-item');
  }
  target.appendChild(item);
}