const numbers = [];
while (true) {
  const input = prompt("Enter a number:");
  if (input === null) {
    document.querySelector("#message").textContent = "Input cancelled. Check the console for entered numbers.";
    break;
  }
  const number = Number(input);
  if (input.trim() === "" || !Number.isFinite(number)) {
    alert("Please enter a valid number.");
    continue;
  }
  if (numbers.includes(number)) {
    alert(`${number} has already been given.`);
    break;
  }
  numbers.push(number);
}

numbers.sort((a, b) => a - b);
console.log(numbers);
