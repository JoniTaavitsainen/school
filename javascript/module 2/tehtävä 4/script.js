const numbers = [];
let cancelled = false;
while (true) {
  const input = prompt("Enter a number (0 ends input):");
  if (input === null) {
    cancelled = true;
    break;
  }
  const number = Number(input);
  if (input.trim() === "" || !Number.isFinite(number)) {
    alert("Please enter a valid number.");
    continue;
  }
  if (number === 0) break;
  numbers.push(number);
}

numbers.sort((a, b) => b - a);
console.log(numbers);
if (cancelled) document.querySelector("#message").textContent = "Input cancelled. Check the console for entered numbers.";
