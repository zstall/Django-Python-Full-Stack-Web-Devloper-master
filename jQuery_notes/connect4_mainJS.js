
var player1 = prompt("Player One: Enter your name, you will be blue");
var player1Color = "rgb(86, 151, 255)";

var player2 = prompt("Player Two: Enter your name, you will be red");
var player2Color = "rgb(237, 45, 73)";

var game_on = true;
var table = $('table tr');


// create a function that will report winning move to the console
function reportWin(rowNum, colNum) {
  console.log("You won starting at this row, col");
  console.log(rowNum);
  console.log(colNum);
}


// funtion that given a row and column index will change that button to a specified player1Color
function changeColor(rowIndex, colIndex, color) {
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', color);
}

// create a function tat will return the current color of a button
function returnColor(rowIndex, colIndex) {
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

// function looks for the first row in a column, from the bottom up that is grey
function checkBottom(colIndex) {
  // var colorReport = returnColor(5, colIndex); NOT NEEDED????
  for (var r = 5; r > -1; r--) {
    var colorReport = returnColor(r, colIndex)
    if (colorReport === 'rgb(128, 128, 128)') {
      return r;
    }
  }
}

function colorMatchCheck(one, two, three, four) {
  return (one === two && one === three && one === four && one !== 'rgb(128, 128, 128)' && one !== undefined);
}

// check for horizontal wins
function horizontalWinCheck() {
  for (var row = 0; row < 6; row++) {
    for (var col = 0; col < 4; col++) {
      if (colorMatchCheck(returnColor(row, col), returnColor(row, col+1), returnColor(row, col+2), returnColor(row, col+3))) {
        console.log('horiz');
        reportWin(row,col);
        return true;
      } else {
        continue;
      }
    }
  }
}

// check for a vertical
function verticalWinCheck() {
  for (var col = 0; col < 6; col++) {
    for (var row = 0; row < 4; row++) {
      if (colorMatchCheck(returnColor(row, col), returnColor(row+1, col), returnColor(row+2, col), returnColor(row+3, col))) {
        console.log('vert');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}

// check for diagonal Wins
function diagonalWinCheck() {
  for (var col = 0; col < 5; col++) {
    for (var row = 0; row < 7; row++){
      if (colorMatchCheck(returnColor(row,col),returnColor(row+1,col+1),returnColor(row+2,col+2),returnColor(row+3,col+3))) {
          console.log('diagonal');
          reportWin(row,col);
          return true;
      } else if (colorMatchCheck(returnColor(row,col),returnColor(row-1,col+1),returnColor(row-2,col+2),returnColor(row-3,col+3))) {
        console.log('diagonal');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}


// Game logic
var currentPlayer = 1;
var currentName = player1;
var currentColor = player1Color;

$('h3').text(player1+" it is your turn, choose a column!");


$('.board button').on('click',function(){
  var col = $(this).closest('td').index();
  var bottomAvail = checkBottom(col)
  changeColor(bottomAvail,col,currentColor);
  if(horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()){
    $('h1').text(currentName+" You have won! Refresh page to play again!");
    $('h3').fadeOut('fast');
    $('h2').fadeOut('fast');
  }

  currentPlayer *= -1;
  if (currentPlayer === 1) {
    currentName = player1;
    $('h3').text(currentName+" it is your turn.")
    currentColor = player1Color;
  }else {
    currentName = player2;
    $('h3').text(currentName+" it is your turn.")
    currentColor = player2Color;
  }
})
