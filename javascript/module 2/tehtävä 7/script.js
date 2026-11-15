function rollDie(sides) {
  return Math.floor(Math.random() * sides) + 1;
}

const input = prompt("How many sides does the die have?");
const sides = Number(input);
if (input === null || input.trim() === "" || !Number.isSafeInteger(sides) || sides < 1) {
  document.querySelector("#message").textContent = "Please enter a positive whole number of sides.";
} else {
  const list = document.querySelector("#rolls");
  let roll;
  do {
    roll = rollDie(sides);
    const item = document.createElement("li");
    item.textContent = roll;
    list.appendChild(item);
  } while (roll !== sides);
}
