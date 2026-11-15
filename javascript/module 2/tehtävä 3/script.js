const dogs = [];
for (let i = 1; i <= 6; i++) {
  const name = prompt(`Name of dog ${i}:`);
  if (name === null || name.trim() === "") {
    document.querySelector("#message").textContent = "Please enter all six dog names.";
    break;
  }
  dogs.push(name.trim());
}

if (dogs.length === 6) {
  dogs.sort((a, b) => b.localeCompare(a));
  const list = document.querySelector("#dogs");
  for (const name of dogs) {
    const item = document.createElement("li");
    item.textContent = name;
    list.appendChild(item);
  }
}
