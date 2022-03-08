### Hash Table

### Q1:

In this kata, you've to count lowercase letters in a given string and return the letter count in a hash with 'letter' as key and count as 'value'. The key must be 'symbol' instead of string in Ruby and 'char' instead of string in Crystal.

### Solution

**Time Complexity = O(N)**  
**Space Complexity = O(N)**

```
function letterCount(s){
  //your code here
  let hashTable = {};

  for(let i=0; i<s.length; i++){

    if(hashTable[s[i]]) {
      hashTable[s[i]]++;
    } else {
      hashTable[s[i]] = 1;
    }
  }

  return hashTable;
}

```

### Q2:

Your start-up's BA has told marketing that your website has a large audience in Scandinavia and surrounding countries. Marketing thinks it would be great to welcome visitors to the site in their own language. Luckily you already use an API that detects the user's location, so this is an easy win.

**The Task**  
Think of a way to store the languages as a database (eg an object). The languages are listed below so you can copy and paste!
Write a 'welcome' function that takes a parameter 'language' (always a string), and returns a greeting - if you have it in your database. It should default to English if the language is not in the database, or in the event of an invalid input.

**The Database**  
english: 'Welcome',
czech: 'Vitejte',
danish: 'Velkomst',
dutch: 'Welkom',
estonian: 'Tere tulemast',
finnish: 'Tervetuloa',
flemish: 'Welgekomen',
french: 'Bienvenue',
german: 'Willkommen',
irish: 'Failte',
italian: 'Benvenuto',
latvian: 'Gaidits',
lithuanian: 'Laukiamas',
polish: 'Witamy',
spanish: 'Bienvenido',
swedish: 'Valkommen',
welsh: 'Croeso'

### Solution

**Time Complexity = O(1)**  
**Space Complexity = O(1)**

```
function greet(language) {

  let hashTableLanguage = {english: 'Welcome',czech: 'Vitejte',danish: 'Velkomst',dutch: 'Welkom',
                           estonian: 'Tere tulemast',finnish: 'Tervetuloa',flemish: 'Welgekomen',
                           french: 'Bienvenue',german: 'Willkommen',irish: 'Failte',
                           italian: 'Benvenuto',latvian: 'Gaidits',lithuanian: 'Laukiamas',
                           polish: 'Witamy',spanish: 'Bienvenido',swedish: 'Valkommen',welsh: 'Croeso'}

  if(hashTableLanguage[language]) {
    return hashTableLanguage[language]
  } else {
    return "Welcome"
  }
}
```

### Q3:

Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.

### Solution

**Time Complexity = O(N<sup>2</sup>)**  
**Space Complexity = O(1)**

```
function getCount(str) {
  var vowelsCount = 0;
  var vowels = ["a","e","i","o","u"];
  for(var i = 0;i < str.length;i++){
    for(var j=0;j<vowels.length;j++){
      if(str[i] === vowels[j]){
        vowelsCount++;
      }
    }
  }

  return vowelsCount;
}
```

[Clock in Mirror](https://www.codewars.com/kata/56548dad6dae7b8756000037/python)

Peter can see a clock in the mirror from the place he sits in the office. When he saw the clock shows 12:22  
He knows that the time is 11:38 in the same manner:  
05:25 --> 06:35  
01:50 --> 10:10  
11:58 --> 12:02  
12:01 --> 11:59

Please complete the function WhatIsTheTime(timeInMirror), where timeInMirror is the mirrored time (what Peter sees) as string.  
Return the real time as a string. Consider hours to be between 1 <= hour < 13.  
So there is no 00:20, instead it is 12:20. There is no 13:20, instead it is 01:20.

### Solution

```
def what_is_the_time(time_in_mirror):
  h, m = time_in_mirror.split(':')
  s = int(h) * 60 * 60 + int(m) * 60
  t = 86400 - s
  return datetime.datetime.fromtimestamp(t).strftime('%I:%M')
```
