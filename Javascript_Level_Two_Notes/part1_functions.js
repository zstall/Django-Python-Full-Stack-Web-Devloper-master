function hello (){
  console.log("hello world");
}

function helloName(name) {
  console.log("Hello " + name);
}

function addNum(num1, num2) {
  console.log(num1+num2);
}

// This will make sure that No Name is passed as parameter if nothing is entered
function helloSomeone(name="No Name") {
  console.log("Hello " + name);
}

// need to use return to have function return a result
function formal(name="Sam", title="Sir") {
  return(title+" "+name);
}

function tmiesFive(numInput) {
  var result = numInput * 5;
  return result;
}
// global scope var

var v = " GLOBAL V"
var stuff = "GLOBAL STUFF"

function fun(stuff) {
  console.log(v);
  stuff = "Reasign stuff inside func";
  console.log(stuff);

}
