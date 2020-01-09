# Guessing the number

This program:

* exercises your understanding of the `if` statement
* introduces the `while` loop
* uses `input`
* uses `print`
* uses `random` and `randint`

The program implements a guess-the-number game where a secret number within a known range is selected. 

The user attempts to guess the value of the secret number. 

The program issues "higher" or "lower" hints to guide the user to the solution. 

The program reports how many guesses were required to guess the secret number.

## Sample output

```text
Guess a number from 1 to 128: 64
Lower
Guess a number from 1 to 128: 32
Lower
Guess a number from 1 to 128: 16
Lower
Guess a number from 1 to 128: 8
Higher
Guess a number from 1 to 128: 12
Lower
Guess a number from 1 to 128: 10
Higher
Guess a number from 1 to 128: 11
You guess it in 7 turns
```

## Top level outline

1. Set up needed state: turn counter, secret number, guess.
2. `while` the guess is not equal to the secret number loop giving hints or reporting win. If a win, somehow stop the loop.

## Outline of loop

1. Ask for a guess.
2. Increment turn counter.
3. Test for higher.
4. Test for lower.
5. If neither of the above, must be a win.

## Calculating the secret number

```python
import random
```

gives you access to the random number generator library.

The function: `randint()` takes two arguments - the minimum and maximum values (inclusive).

