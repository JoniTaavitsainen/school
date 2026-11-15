let name = prompt("What is your name?");
document.querySelector("#result").textContent = name === null ? "No name was entered." : `Hello, ${name}!`;