const input = prompt("How many dice should be rolled?");
const count = Number(input);
const result = document.querySelector("#result");

if (input === null || input.trim() === "" || !Number.isSafeInteger(count) || count < 0) {
  result.textContent = "Please enter a non-negative whole number of dice.";
} else {
  let sum = 0;
  for (let i = 0; i < count; i++) {
    sum += Math.floor(Math.random() * 6) + 1;
  }
  result.textContent = `The sum is ${sum}.`;
}
