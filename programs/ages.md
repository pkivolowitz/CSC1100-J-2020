# Ages

This program offers practice with the simplest `if` statement.

Here is a flow chart of the simplest `if`.

![if](../pics/if.png)

Expressing this in code:

```python
if decision:
    process
```

In the above, `process` standards for 1 or more lines of Python code.

## Write a program

Use `input()` twice to prompt for two ages. Assign each age into its own variable, perhaps `age1` and `age2`.

Note `input()` returns strings, but you need the data as numbers - you must convert these yourself as in the following sample code:

```python
# This returns a string into age1
age1 = input('Enter the age of person 1: ')
# This returns a number into age1
age1 = int(input('Enter the age of person 1: '))
```

Then, write a series of `if` statements that will test for the following conditions:

* If both ages are 16 or over, print `Both can drive.`
* If either age is 21 or greater, print `At least one can rent a car`.
* If neither is 35 or older, print `Neither can be President`.
* If **only one** of the two ages is 25 or more print `Exactly one can be a senator`.

Test your program with different ages.

