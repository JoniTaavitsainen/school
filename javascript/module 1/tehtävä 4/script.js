const name = prompt("Enter the student's name:");
const result = document.querySelector("#result");

if (name === null || name.trim() === "") {
  result.textContent = "No student name was entered.";
} else {
  const draw = Math.floor(Math.random() * 4) + 1;
  let house;
  switch (draw) {
    case 1:
      house = "Gryffindor";
      break;
    case 2:
      house = "Slytherin";
      break;
    case 3:
      house = "Hufflepuff";
      break;
    case 4:
      house = "Ravenclaw";
      break;
  }
  result.textContent = `${name.trim()}, you are ${house}.`;
}
