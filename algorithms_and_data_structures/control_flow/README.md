### Control Flow   
### if:  
The code below runs and displays _This block of code is running_ because the condition specified is true
```
var value = true;
if(value) {
  console.log("This block of code is running");
}
```

### if-else:  
In the code above, when the statement is false, the code execution ends.  
But with _if-else_ statement, if the condition is false, code in _else_ block runs

```
var value = false;
if(value) {
  console.log("I will not run because I am true");
} else {
  console.log("My block runs because");
}
```
### switch:  
The statement compares the value in the variable to the cases defined in each _case_.  
If a case matches, the code associated executes.  
If it does not, then the code in _default_ block runs.

```
var favoriteFruit = "Orange"

switch(favoriteFruit) {
  case "Grapes":
    console.log("Grapes fruit here");
    break;
  case "Pineapple":
    console.log("Pina pineapple here");
    break;
  case "Orange":
    console.log("Orango orange");
    break;
  default:
    console.log("Neither grapes, pineapple, nor orange");
}
```

