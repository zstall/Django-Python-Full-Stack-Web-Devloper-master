var headOne = document.querySelector("#one");
var headTwo = document.querySelector("#two");
var headThree = document.querySelector("#three");

headOne.addEventListener("mouseover", function(){
  headOne.textContent = "You did it!";
  headOne.style.color = "blue";
})
headOne.addEventListener("mouseout", function(){
  headOne.textContent = "HOVER OVER ME!";
  headOne.style.color = "black";
})

headTwo.addEventListener("mousedown", function(){
  headTwo.textContent = "Click Monster!";
  headTwo.style.color = "red";
})

headTwo.addEventListener("mouseup", function(){
  headTwo.textContent = "CLICK ME!";
  headTwo.style.color = "black";
})


headThree.addEventListener("dblclick", function(){
  headThree.textContent = "Nice! Double Click! But I'm Stuck :(";
  headThree.style.color = "green";
})
