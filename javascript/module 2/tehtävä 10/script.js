function askCount(question, minimum) {
  while (true) {
    const input = prompt(question);
    if (input === null) return null;
    const count = Number(input);
    if (input.trim() !== "" && Number.isSafeInteger(count) && count >= minimum) {
      return count;
    }
    alert(`Enter a whole number of at least ${minimum}.`);
  }
}

function runVote() {
  const candidateCount = askCount("How many candidates?", 1);
  if (candidateCount === null) return false;
  const candidates = [];
  for (let i = 1; i <= candidateCount; i++) {
    while (true) {
      const input = prompt(`Name for candidate ${i}:`);
      if (input === null) return false;
      const name = input.trim();
      if (!name || candidates.some((candidate) => candidate.name.toLowerCase() === name.toLowerCase())) {
        alert("Enter a non-empty, unique candidate name.");
        continue;
      }
      candidates.push({name, votes: 0});
      break;
    }
  }

  const voterCount = askCount("How many voters?", 0);
  if (voterCount === null) return false;
  for (let i = 1; i <= voterCount; i++) {
    while (true) {
      const input = prompt(`Voter ${i}, enter a candidate name or leave blank for an empty vote:`);
      if (input === null) return false;
      const vote = input.trim();
      if (vote === "") break;
      const candidate = candidates.find((entry) => entry.name.toLowerCase() === vote.toLowerCase());
      if (candidate) {
        candidate.votes++;
        break;
      }
      alert("Candidate not found. Enter a listed candidate's name or leave the vote empty.");
    }
  }

  candidates.sort((a, b) => b.votes - a.votes);
  const winners = candidates.filter((candidate) => candidate.votes === candidates[0].votes);
  if (winners.length === 1) {
    console.log(`The winner is ${winners[0].name} with ${winners[0].votes} votes.`);
  } else {
    console.log(`The vote is tied between ${winners.map((candidate) => candidate.name).join(", ")} with ${winners[0].votes} votes each.`);
  }
  console.log("results:");
  for (const candidate of candidates) {
    console.log(`${candidate.name}: ${candidate.votes} votes`);
  }
  return true;
}

if (!runVote()) {
  document.querySelector("#message").textContent = "Voting was cancelled.";
}
