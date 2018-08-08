/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// While Loop
var num = 1;
while (num < 6) {
  console.log(num+". while hello");
  num += 1;
}

// For Loop
for (var i = 1; i < 6; i++) {
  console.log(i+". for hello");
}
/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop
var oddNum = 1;
while (oddNum < 26) {
  if (oddNum%2 !== 0) {
    console.log("while loop: "+oddNum);
  }
  oddNum += 1;
}

// METHOD TWO
// For Loop
for (var i = 1; i < 26; i+=2) {
  console.log("for loop: "+i);
}
