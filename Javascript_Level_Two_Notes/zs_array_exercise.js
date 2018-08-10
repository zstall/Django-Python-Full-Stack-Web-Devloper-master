


// Create a array for the student roster
var studentRoster = []


// Adding a student
function addStudent(name){
  studentRoster.push(name)
  alert("Student Added")
}

// Remove a student
function removeStudent(name){
  // Check that name is on roster, if not return to task prompt
  if (studentRoster.indexOf(name)<0) {
    alert("That student is not on the list, click okay to go back.")
  }else {
    studentRoster.splice(studentRoster.indexOf(name),1);
    alert("Student Removed");
  }
}

// function to display roster to the log
function displayRoster(){
  for (var stu in studentRoster) {
    console.log(studentRoster[stu]);
    }
}


// prompt the user to start the app
launch = prompt("Would you like to launch Student Roster (y/n)?")
if (launch == "y" || launch=="Y") {
  launch = true;
}else {
  launch = false;
}

// when app launced will repeat while loop until user quits
while (launch) {
  // get what the user wants to do, add, remove, diplay or quit
  task = prompt("Type option of what you would like to do: add, remove, display, quit")

  // add a student
  if (task.toLowerCase() == "add") {
    n = prompt("Enter student name: ");
    addStudent(n);
  // remove a student
  }else if (task.toLowerCase() == "remove") {
    r = prompt("Enter student name to be removed: ");
    removeStudent(r);
  // display students roster
  }else if (task.toLowerCase() == "display") {
    displayRoster();
  // quit app
  }else if (task.toLowerCase() == "quit"){
    // make sure user is ready to quit
    q = prompt("Sure you want to quit? y/n")
    if (q == "y") {
      launch = false;
    }
  // check for bad command
  }else {
    alert("Command not recognized.")
  }
}
