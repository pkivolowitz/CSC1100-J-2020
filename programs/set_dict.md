# Sets and Dictionaries and File IO - OH MY!

We are going to write two programs:

* Both will use File IO (reading)
* One will exercise sets
* The other will exercise dictionaries

## The data

File `bn.txt` contains popular baby names. It comes from another file that breaks down baby names by reported ethnicity.

Here are the first few lines:

```text
GERALDINE
GIA
GIANNA
GISELLE
GRACE
```

## Reading lines from a file

This is not meant to replace reading about file IO in the book - this is a simple description of reading whole lines.

### Open the file for reading

```python
file = open('path to file', 'r')
```

### Reading all the lines

```python
for l in file:
    # do something with l - note you may need to strip new lines from l
```

In the case of this program, add the name (it's on a line by itself) to the set or dictionary. Note that you may have to strip new line characters using `rstrip()` as in:

```python
l = l.rstrip()
```

### Closing the file

```python
file.close()
```

## Sets program

Add each name in the file to a set.

THEN, loop asking the user to enter a name.

If the name is `quit`, exit the loop.

Otherwise check if the name (made uppercase) is in the set. Print the result.

### Example



```text
19418 names were read from the file
1775  names were unique
Enter a name (uppercase): GEORGE
GEORGE was in the file
Enter a name (uppercase): GREGOR
GREGOR was not in the file
Enter a name (uppercase): QUIT
```

### Counters

Set up a line counter - that's the one that results in 19418.

The number of unique names comes from the finished set.

### Zybooks

For help, reread chapter 3.3.

## Dictionary program

A dictionary maps a key to a value. Sets only have keys.

Make a dictionary where the key is a name. The vaue will be how many times you've read it.

### Example

```text
19418 names were read from the file
1775  names were unique
Enter a name (uppercase): GEORGE
GEORGE was in the file 30 times
Enter a name (uppercase): MARY
MARY was in the file 9 times
Enter a name (uppercase): MARVIN
MARVIN was in the file 8 times
Enter a name (uppercase): JOSEPHUS
JOSEPHUS was not in the file
Enter a name (uppercase): QUIT
```
