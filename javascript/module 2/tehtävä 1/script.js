const numbers = [];
for (let i = 1; i <= 5; i++) {
  const input = prompt(`Enter number ${i}:`);
  const number = Number(input);
  if (input === null || input.trim() === "" || !Number.isFinite(number)) {
    document.querySelector("#message").textContent = "Please enter five valid numbers.";
    break;
  }
  numbers.push(number);
}

if (numbers.length === 5) {
  for (let i = numbers.length - 1; i >= 0; i--) {
    console.log(numbers[i]);
  }
}
