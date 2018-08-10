// main js

// Createa a variable for the restart button
var restart = document.querySelector("#btn");
// create an array of the "sqaures"
var squares = document.querySelectorAll("td");


// this function walks steps through each square in the board and resets it to have
// no text.
function resetBoard() {
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = "";
  }
}


// This function checks a square to see what is the current text, and will switch to the
// next option on each click by the player
function playerClick() {
  if (this.textContent === "") {
    this.textContent = "X";
  }else if (this.textContent === "X") {
    this.textContent = "O";
  }else{
    this.textContent = ""
  }
}

// See if the lisenter clicks restart, if they do call resetBoard function
restart.addEventListener("click", resetBoard)

// Loop through each "square" and add a even listener to see where the player clicks
for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener("click", playerClick)
}
