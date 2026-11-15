const numbers = [];
const result = document.querySelector("#result");

for (let i = 1; i <= 3; i++) {
  const input = prompt(`Enter integer ${i}:`);
  if (input === null || input.trim() === "" || !Number.isSafeInteger(Number(input))) {
    result.textContent = "Please enter three valid integers.";
    break;
  }
  numbers.push(Number(input));
}

if (numbers.length === 3) {
  const sum = numbers[0] + numbers[1] + numbers[2];
  const product = numbers[0] * numbers[1] * numbers[2];
  for (const text of [`Sum: ${sum}`, `Product: ${product}`, `Average: ${sum / 3}`]) {
    const paragraph = document.createElement("p");
    paragraph.textContent = text;
    result.appendChild(paragraph);
  }
}
