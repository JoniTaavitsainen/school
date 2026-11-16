'use strict';

const trigger = document.querySelector('#trigger');
const image = document.querySelector('#target');

trigger.addEventListener('mouseenter', () => {
  image.src = 'img/picB.jpg';
});

trigger.addEventListener('mouseleave', () => {
  image.src = 'img/picA.jpg';
});