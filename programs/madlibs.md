#  Mad Libs

In a Mad Lib, random words are substituted into a template for form nonsense sentences.

## Template

Our template will be:

*subject adverb1 verb pronoun adverb2 noun*

For example:

They quickly drove their dirty car.

Or choose a template of your own such as:

*subject adverb verb a adverb noun*

John unexpectedly dropped a red orange.

## Lists

Make lists of appropriate words of each type. 

For example:

```python
subjects = [ 'John', 'Mary', 'The duck', 'He', 'She', 'They' ]
```

## Create the Mad Lib

From each list, in the right order, select a value at random to use.

There is another feature of `random` we can use as in this example:

```python
random.choice(subjects)
```

returns one of the members of the list `subjects` chosen at random.

By the way, `choices` (note the plural) can return more than one item chosen at random using the optional named parameter `k` as in this example:

```python
random.choices([1, 2, 3, 4, 5], k=3)
```

## Generate (print) more than one mad lib

How about 10 of them?

