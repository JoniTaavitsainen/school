function rollDie() {
  return Math.floor(Math.random() * 6) + 1;
}

const list = document.querySelector("#rolls");
let roll;
do {
  roll = rollDie();
  const item = document.createElement("li");
  item.textContent = roll;
  list.appendChild(item);
} while (roll !== 6);
