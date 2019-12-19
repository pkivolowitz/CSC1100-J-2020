# Day 1 experiments

These snippets are intended to be annotated by the instructor. After each, experiment yourself.

Each of these demonstrate one or more important concepts.

```python
>>> 10
10
>>> 10 + 10
20
>>> a
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> 'a'
'a'
>>> 'a' + 10
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 'a' + 'b'
'ab'
>>>
```

```python
>>> 9plan = 'movie'
File "<stdin>", line 1
9plan = 'movie'
^
SyntaxError: invalid syntax
>>> plan9 = 'movie'
>>> plan9
'movie'
>>>
```

```python
>>> apples
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'apples' is not defined
>>> apples = 10
>>> apples
10
>>> apples = apples + 1
>>> apples
11
>>>
```

```python
>>> print(apples)
11
>>> oranges = 4
>>> print(apples, oranges)
11 4
>>> print(apples + oranges)
15
>>>
```

```python
>>> flush = [ '3S', '6S', '4S', '10S', 'QS' ]
>>> flush
['3S', '6S', '4S', '10S', 'QS']
>>> flush[0]
'3S'
>>> flush[21]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> flush[-1]
'QS'
>>> flush[1:2]
['6S']
>>> flush[1:3]
['6S', '4S']
>>> flush[3:]
['10S', 'QS']
>>>
```

```python
>>> abs(-1)
1
>>> 2 * 3 + 1
7
>>> (2 * 3) + 1
7
>>> 2 * (3 + 1)
8
>>>
```

```python
>>> [1,2] * 4
[1, 2, 1, 2, 1, 2, 1, 2]
>>> 'a' * 4
'aaaa'
>>> 'na' * 16 + ' batman!'
'nananananananananananananananana batman!'
>>> 
```
