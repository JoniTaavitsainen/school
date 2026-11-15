const input = prompt("Enter a year:");
const year = Number(input);
const result = document.querySelector("#result");

if (input === null || input.trim() === "" || !Number.isSafeInteger(year)) {
  result.textContent = "Please enter a valid whole year.";
} else {
  const leapYear = year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0);
  result.textContent = `${year} is ${leapYear ? "" : "not "}a leap year.`;
}
