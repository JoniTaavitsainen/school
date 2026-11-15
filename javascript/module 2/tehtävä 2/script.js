const input = prompt("How many participants?");
const count = Number(input);
const message = document.querySelector("#message");

if (input === null || input.trim() === "" || !Number.isSafeInteger(count) || count < 0) {
  message.textContent = "Please enter a non-negative whole number.";
} else {
  const names = [];
  for (let i = 1; i <= count; i++) {
    const name = prompt(`Name of participant ${i}:`);
    if (name === null || name.trim() === "") {
      message.textContent = "A participant name was not entered.";
      break;
    }
    names.push(name.trim());
  }
  if (names.length === count) {
    names.sort((a, b) => a.localeCompare(b));
    const list = document.querySelector("#participants");
    for (const name of names) {
      const item = document.createElement("li");
      item.textContent = name;
      list.appendChild(item);
    }
  }
}
