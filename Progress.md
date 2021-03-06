# Progress

## January 8

On this day:
* We learned how to purchase and enroll in the class textbook.
* We went over the syllabus and learned that we can use Google Calendar to make appointments with the Professor.
* We installed Python 3.7, VS Code and some of the libraries we need.
* The Mac instructions contained a broken link to `scipy`. This has been fixed.
* We learned about these data types: numbers, strings and Booleans.
* We are able to enter the command line on Windows and on the Mac.
* We are able to enter Python interactive on both platforms.
* We learned we can exit interactive Python using `exit()` or `^D` on the Mac or `^Z return` on Windows.
* On the Mac we learned we must use `python3` and `pip3` rather than `python` and `pip`.
* We learned about many operators including +, -, /, *, // and %.
* We learned about logical operators `and` and `or`.
* We saw the simplest forms of `print()` and learned that it is an example of a *function*.
* We saw a minimal example of writing a program in VS Code and running it from there.
* We saw a *flow chart*.
* We used flow charts to diagram three variations on an `if` statement.
* We examined one form a little more closely.

## January 9

On this day:
* We reviewed. 
* We wrote program "ages" which used `input()` and simple `if` statements.
* We wrote program "temperatures" which said snarky things about various temperature ranges and finally, converted the temperature into Celsius.
* We learned about `while` loops, using code examples, flow charts and RL examples.
* We retrofitted a `while` loop into the "temperatures" program.
* We learned how to print several "things" on one line using commas in a call to `print()`.
* We heard that feet, degrees (in a circle) and degrees Farenheit are completely made up and that meters, radians and degrees Celsius are real. We also heard about Kelvin. Degrees Kelvin are real too.
* Chapter 1 was assigned as homework.
* We demo'd a subchapter from the book.

## January 10

On this day we:

* reviewed
* learned about `import` - specifically we imported `random`
* learned how to use `randint()`
* learned what `determinism` is and how challenging it can be for computers to generate "random" numbers
* learned how important random numbers are to science as they are the basis of much of how simulation works
* wrote three programs featuring while loops
    * We wrote a program that "rolled a 100 sided die" until a value of 100 came up. We counted the number of times the loop executed.
	* We modified this program to run 1,000,000 times averaging the results of each trial. This introduced us to nested `while` loops.
	* We wrote a number guessing game in the range of 1 to 128. The program printed "higher" or "lower" depending on user input
* were reminded that chapter 1 of the reading is due at 11:59 PM
* were reminded that chapter 2 of the reading is due Monday night at 11:59 PM
* were reminded that Monday will start our almost-daily quizzes. Monday's quiz will cover chapter 1

## January 13

On this day we:

* reviewed
* learned about lists:
    * Making an empty list
    * Adding to a list using `append`
    * Getting the length of a list using `len`
    * Indexing into a list
    * Slicing a list
    * Making a list from `range`
    * Shuffling a list
    * Tuples are like lists but are "read only"
* learned that multiple variables can be assigned using commas
* learned the `for` loop
* wrote a program to print out a hand of 5 playing cards
* took a quiz on chapter 1
* were reminded chapter 2 is due tonight
* were assigned chapters 3.1 through 3.5.

## January 14

We reviewed. 

Today we practiced:

* nested loops
* formatted output
* making lists from a range

We wrote two more programs:

* Printing a multiplication table
* Mad libs

We learned about:

* `random.choice()`
* `random.choices()`
* list `index()`
* list `count()`
* list `sort()`
* list `pop()`
* list `remove()`
* list `extend()`
* list `insert()`

We saw:

* George Carlin's differences between baseball and football
* Abbot and Costello's Who's on First
* A teaser about `matplotlib`

## January 15

We reviewed. During review, in answer to a question, we covered `namedtuple`.

On this day we learned:

* How to open a file for reading
* How to read whole lines from a file
* How to close a file
* How to use string methods `rstrip()` (and consequently `lstrip()`)
* That sets can record that some item is `in` a set (or `not in`)
* How to define a set and various set operations.

We wrote a program that read names from a file and added them to a set. Then, we could search the set for user inputted names and could report if the name was in the set or not.

We began learning about dictionaries.

## January 16

* We reviewed. We reheard that the important difference between sets and dictionaries are that sets can only record membership (or not). Dictionaries not only record membership, they also can deliver a value mapped from a particular key. 
* We wrote the dictionary practice program. The most important thing we learned is that before a key can be accessed it must first be in the dictionary.
* Chapters 4 and 5 were assigned but as they cover material we have already learned, the due date is far away (the 24th). Chapter 6 is new material and it was assigned for Tuesday, the 21st.
* We introduced the `csv` module
* We learned about `csv.reader()`
* We learned about `csv.DictReader()`
* We learned that Excel can both read and write csv files.
* WE READ AND PARSED OUR FIRST CSV FILE!

## January 17

On this day we:

* reviewed
* learned about `sys.argv` which *really* adds to our power by allowing us to avoid hard coding file names and giving other command line options.
* learned the importance of *looking before leaping* - we check for the presence of arguments before using them.
* learned about exiting a program early with `exit()`.
* learned how important it is to give meaningful error messages.
* learned about functions:
  * how to define them
  * how to call them
  * how to pass and use arguments
  * how to return values
  * how they are not executed immediately when they are encountered by python but are stored and remembered for later
* revisited the card dealing program - this time using better design leveraging functions. Our goal is not only to deal a hand but to also evaluate the hand.
* learned about and practiced using compounded data structures like lists that contain dictionaries.
* remember that chapter 6 (functions) is due on Tuesday - quiz on Wednesday

## January 20

On this day we:

* Reviewed
* Learned about unit testing
* Learned how to use `pytest` to perform unit testing
* Saw how to install pytest (`pip install pytest`)

## January 21

On this day we:

* Reviewed (in particular `pytest`)
* Learned about `continue` and `break`
* Wrote a program in incremental steps ("Write a Little. Test a Little")
    * We read and printed date from a DictReader
    * We made lists out of the data from a DictReader
    * We converted the data reading / list making into its own function returning the finished lists

## Note for future

Work these into the remaining term:

* os
* shutil
