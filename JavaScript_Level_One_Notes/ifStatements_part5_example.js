var hot = false;
var temp = 30;

if (temp>80) {
  console.log("Hot Outside!");
} else if (temp<=80 && temp>50) {
  console.log("Average Temp Outside");
} else if (temp<=50 && temp>32) {
  console.log("It\'s pretty cold outside");
} else {
  console.log("It is very cold out!");
}
