# Word chain

### Description

Two participants play a linguistic game. A list of *N* words is given at the beginning of the game.
The first player chooses a random word *w1* and crosses out one random letter from it to get another word *w2* from this list. After that, the movie goes to another player, and he tries to do the same with the word *w2*.
The game ends in one of two cases:
- One letter is left.
- No letters can be crossed out to get another word from the dictionary.

Determine the length of the maximum chain that can be reached in this game at given words.

### Input data

The input file consists of *N + 1* rows.
- The first line contains *N* - the number of words in the dictionary, *1 < N < 10^5*.
- Each of the following N lines contains a word from 1 to 50 characters long, which consists of small Latin letters from a to z.

### Output data

The length of the longest word chain.
