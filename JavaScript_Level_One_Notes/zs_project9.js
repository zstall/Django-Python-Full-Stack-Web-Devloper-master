var fName = prompt("Enter First Name: ")
var lName = prompt("Enter Last Name: ")
var age = prompt("Enter Age: ")
var height = prompt("Enter Height in cm: ")
var pet = prompt("Enter your pets name: ")
alert("Thank you for the information!")


if (fName[0].toLowerCase() == lName[0].toLowerCase() &&
    age > 20 &&
    age < 30 &&
    height >= 170 &&
    "y" === pet.slice(-1).toLowerCase()) {
  console.log("Congrats spy, you have unlocked the secret message!");
}
