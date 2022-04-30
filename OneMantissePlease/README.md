# One Mantissa Please

## Challenge
```
I'll have one mantissa to go, please! (Note: the correct answer is the smallest positive integer value.) 
```

## Solution

Mantissa in computer science are is part of a number in scientific notation or floating-point representation, consisting of its significant digits. ([Source](https://en.wikipedia.org/wiki/Significand))

This means, we are dealing with some kind of floating-point problem.
When connecting to the server we get a message
```
we've got a funky shell over here, and we're going to feed it your input!
the shell will run the following:
console.log(%d == (%d + 1));
And the flag is `flag{<md5>}, where <md5> is the md5sum of the smallest integer input that prints true!
>>>
```

So, we need to find the smallest integer i for that is `i == i+1` in JavaScript.  
Sounds counter-intuitive and my first try was to let me bruteforce the solution by running [checkForIntegerErrors.js](checkForIntegerErrors.js) after I found a number from [this stackoverflow-thread](https://stackoverflow.com/a/3439981).

In the meantime I tried to find a solution, that does not rely on brutforcinf my way through and found the JavaScript Property [Number.MAX_SAFE_INTEGER](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER)  

```
The Number.MAX_SAFE_INTEGER constant represents the maximum safe integer in JavaScript (2^53 - 1).
```
The example code gave us the anser right away
```
const x = Number.MAX_SAFE_INTEGER + 1;
const y = Number.MAX_SAFE_INTEGER + 2;

console.log(Number.MAX_SAFE_INTEGER);
// expected output: 9007199254740991

console.log(x);
// expected output: 9007199254740992

console.log(x === y);
// expected output: true
```
Answer: `9007199254740992`

Checking with the system we can confirm, that this number does indeed fulfil the challenge
```
we've got a funky shell over here, and we're going to feed it your input!
the shell will run the following:
console.log(%d == (%d + 1));
And the flag is `flag{<md5>}, where <md5> is the md5sum of the smallest integer input that prints true!
>>>9007199254740992
Congrats!
```

Converting the value to md5 (i used https://www.md5hashgenerator.com/) to generate the flag: `flag{3a78300a68de2a1210c9e3726c3cb87a}`

# To be or not to be

## Challenge
```
To be and not to be, that is the question. (Note: the correct input solution to this challenge is alphanumeric.) 
```

## Solution

This challenge is similar to the one described above.
When checking into the system the task was:

```
we've got a funky shell over here, and we're going to feed it your input!
the shell will run the following:
console.log(%s !== (%s));
And the flag is `flag{<md5>}, where <md5> is the md5sum of the input that prints true!
>>>
```

Again it was JavaScript and we assumed it had something to do with the fact that `1 !== '1'`. 
So we had to find some kind of number, that is interpreted differntly as Number as as String.

We checked for solutions like `0b1` for 1 in binary or `0x1` for 1 in Hex, but nothing worked.
We also found, that the solution is indeed alpha-numerical (regex `[A-Za-z0-9]`) and only max 3 chars long.

Having solved the Manitassa-Challenge we had a look into more global JavaScript-Properties and found `Number.NaN` (Not A Number)

NaN was short enough and had enough potential to be treated differently as "number" and as String.

So we check it out and it gave the message
```
we've got a funky shell over here, and we're going to feed it your input!
the shell will run the following:
console.log(%s !== (%s));
And the flag is `flag{<md5>}, where <md5> is the md5sum of the input that prints true!
>>>NaN
Congrats!
```

Creating the md5hash for `NaN` we get the flag `flag{7ecfb3bf076a6a9635f975fe96ac97fd}`

#### After-Challenge correction
While writing this after the challenges are over, I had a deeper look into our solution and tried a bit with local execution:
values like `0b1` and so on should have thrown a positive feedback from my tests
```js
> console.log(0b1 !== '0b1')
true
undefined
> console.log(0x1 !== '0x1')
true
undefined
> console.log(NaN !== 'NaN')
true
undefined
```
but i noticed, that we did use the correct syntax.  
Using the same syntax as in the challenge, our binary and hex-representations of numbers did indeed result in a false (only NaN remained true)
```js
> console.log(0b1 !== (0b1))
false
undefined
> console.log(0x1 !== (0x1))
false
undefined
> console.log(NaN !== (NaN))
true
undefined
```

What I learned. In JavaScript **NaN does not equal NaN**