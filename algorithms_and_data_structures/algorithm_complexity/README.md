### Hash Table   
Q1: In this kata, you've to count lowercase letters in a given string and return the letter count in a hash with 'letter' as key and count as 'value'. The key must be 'symbol' instead of string in Ruby and 'char' instead of string in Crystal.

### Solution  
**Time Complexity = O(N)**

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

Q2: Your start-up's BA has told marketing that your website has a large audience in Scandinavia and surrounding countries. Marketing thinks it would be great to welcome visitors to the site in their own language. Luckily you already use an API that detects the user's location, so this is an easy win.  

**The Task**  
Think of a way to store the languages as a database (eg an object). The languages are listed below so you can copy and paste!
Write a 'welcome' function that takes a parameter 'language' (always a string), and returns a greeting - if you have it in your database. It should default to English if the language is not in the database, or in the event of an invalid input.  

__The Database__  
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