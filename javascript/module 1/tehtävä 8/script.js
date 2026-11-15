const startInput = prompt("Enter the start year:");
const endInput = prompt("Enter the end year:");
const start = Number(startInput);
const end = Number(endInput);
const message = document.querySelector("#message");

if (startInput === null || endInput === null || startInput.trim() === "" ||
    endInput.trim() === "" || !Number.isSafeInteger(start) || !Number.isSafeInteger(end)) {
  message.textContent = "Please enter two valid whole years.";
} else if (start > end) {
  message.textContent = "The start year must not be after the end year.";
} else {
  const list = document.querySelector("#years");
  for (let year = start; year <= end; year++) {
    if (year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0)) {
      const item = document.createElement("li");
      item.textContent = year;
      list.appendChild(item);
    }
    if (year === end) break;
  }
}
