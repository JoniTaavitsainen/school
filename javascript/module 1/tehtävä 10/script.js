const diceInput = prompt("How many dice?");
const sumInput = prompt("What sum are you interested in?");
const dice = Number(diceInput);
const wantedSum = Number(sumInput);
const result = document.querySelector("#result");

if (diceInput === null || sumInput === null || diceInput.trim() === "" ||
    sumInput.trim() === "" || !Number.isSafeInteger(dice) || dice < 1 ||
    !Number.isSafeInteger(wantedSum)) {
  result.textContent = "Enter a positive whole number of dice and a whole-number sum.";
} else {
  const trials = 100000;
  let matches = 0;
  for (let trial = 0; trial < trials; trial++) {
    let sum = 0;
    for (let die = 0; die < dice; die++) {
      sum += Math.floor(Math.random() * 6) + 1;
    }
    if (sum === wantedSum) matches++;
  }
  const probability = (matches / trials * 100).toFixed(2);
  result.textContent = `Probability to get sum ${wantedSum} with ${dice} dice is ${probability}%`;
}
