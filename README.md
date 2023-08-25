# Poker Evaluator

## Overview

The Poker Evaluator is a command-line program that calculates the winning probability for a Texas Hold'em poker hand. By providing two cards and the number of players in the hand, the program will evaluate the hand's strength over multiple simulations and provide a probability of winning, along with an error margin.

## Dependencies

Before running the program, ensure you have the following Python modules installed:

- `random`
- `argparse`
- `itertools`

These dependencies are included in the Python Standard Library and should be available by default.

## Usage

### CLI

Run the program using the following command:

``` 
python3 main.py [c1] [c2] [n_players]
```

Where:
- [c1] is the first card in the hand, e.g. 'AS' for Ace of Spades
- [c2] is the second card in the hand, e.g. '2H' for Two of Hearts
- [n_players] is the number of players in the hand, e.g. '4' for four players

Example usage:

```
python3 main.py TC JD 3
```

This will evaluate the probability of winning with Ten of Clubs and Jack of Diamonds with 3 players in total.

### Output

After running, the program will provide an output similar to:

```
Win probability: 40.91% ± 0.96%
```

## Under the Hood

The program works by simulating numerous poker hands using the provided cards. The evaluation method used is based on scoring different combinations of cards in the board. The better the combination, the lower the score. The program then compares the score of the player's hand against scores of randomly generated hands for other players. After many simulations, it calculates the percentage of times the player's hand wins.

In order to simulate hands efficiently, the program represents decks as sets of bits and derives information from them using bitwise operations. This allows for fast generation of random hands and efficient scoring of hands. Some of the logic can be credited to http://suffe.cool/poker/evaluator.html.