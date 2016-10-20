# Markov Model

### Finding a text to train on
Project Gutenberg<sup id="a1">[1](#f1)</sup> allows to easily access and download books from their website.
Knowing the book id it can be downloaded and cached via ```gutenberg.getBook(id)```
Some straightforward preprocessing is performed on the book to remove the less significant parts, but for better results it is suggested to do a deeper cleanup of the text.

### Preprocessing Tools
In order to easily deal with sentences and paragraphs some preprocessing functions are available:
* ```sentence``` gets rid of all strange characters in a sentence, turns everything to lower case and returns a list of words
* ```paragraph``` performs the same operations as ```sentence``` on every sencence of the given paragraph and returns a list of lists of words
* ```dictionary``` given a preprocessed sentence/paragraph returns an ordered list of unique elements

## Markov Chains
This python implementation of a Markov Chain<sup id="a2">[2](#f2)</sup> allows to (re)train a model on sequences
of characters or words and then generate arbitrarily long sequences through a random walk<sup id="a3">[3](#f3)</sup>.

### Creation
To create an initially random Markov Model it is necessary to provide a dictionary of the elements that will be present in the sequences in the form of an ordered list:
```
dic = ["hey", "jude"]
mm = MarkovModel(dic)
```

### Training
The model can now be trained multiple times on multiple sequences. This will result in updating the internal frequency matrix (number of occurrences of the transaction: "first word" -> "second word") and a recalculation of the transition probability matrix (number of occurrences of the transaction: "first word" -> "second word" / number of occurrences of "first word").
```
mm.update([["hey", "hey", "jude"],["jude", "hey", "jude"]])
mm.update(["jude", "hey", "jude"]*20)
```

### Generating
Generating a sequence is now straightforward: simply call the ```generate()``` method optionally specifying the initial element of the sequence and its length.
```
" ".join(mm.generate(initial="hey", T=15)
```

## Second Order Markov Models
To come...

## Hidden Markov Models
To come...

1. <a id="f1">Project Gutenberg [Website](https://www.gutenberg.org/)</a> [↩](#a1)
1. <a id="f2">Markov Chains on [Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)</a> [↩](#a2)
1. <a id="f3">Random Walk on [Wikipedia](https://en.wikipedia.org/wiki/Random_walk)</a> [↩](#a3)
