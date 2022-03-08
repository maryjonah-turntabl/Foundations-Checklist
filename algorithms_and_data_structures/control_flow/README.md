## Control Flow

### Count-controlled Loop

_for_: Print "I am happy" 5 times

```
for (let i = 0; i < 5; i++) {
  console.log("I am happy")
}
```

### Condition-controlled Loop

_while_: Count down from 5 to 1

```
let number = 5;

while (number > 0) {
  console.log(number);
  number--;
}
```

_do-while_: Prints 5 once and ends the execution of the loop

```
let counter = 5;

do {
   console.log(counter)
   counter++;
} while (counter < 2)
```

### Collection-controlled Loop

_for...in_: Prints the key and value pair in the person object

```
const person = {fname:"John", lname:"Doe", age:25};

for (let x in person) {
  console.log("Key is: " + x);
  console.log("Value is: " + person[x]);
}
```

### Choice-controlled Loop

_if/ else if/ else_: Runs a block of code based on whose' boolean condition returns true

```
let currentDay = "Monday";
let excitementLevel = 0;

if (currentDay == "Monday") {
  excitementLevel = 5;
} else if (currentDay == "Tuesday") {
  excitementLevel = 7;
} else {
  excitementLevel = 10;
}
```

_case...switch_: Runs a block of code based on which case returns true

```
let currentDay = "Monday";
let excitementLevel = 0;

switch(currentDay) {
  case 'Monday':
    excitementLevel = 5;
    break;
  case 'Tuesday':
    excitementLevel = 7;
    break;
  default:
    excitementLevel = 10
}
```
