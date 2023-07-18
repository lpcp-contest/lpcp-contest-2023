# Problem 3

Great news!
Our proposal to build a street connecting point A with point B is approved.
The only problem is that we have to satisfy a few crazy conditions that we threw in at submission time, and the reviewer asked to reuse some existing road parts.

In short, each row and each column of a square grid is associated with an integer, being the number of cells that must contain a road part (what a crazy condition from us).
Point A is on the left of the grid, and point B is on its bottom.
To keep it easy, we can use 6 types of road parts:
- type 1 is `╗`
- type 2 is `║`
- type 3 is `╝`
- type 4 is `╚`
- type 5 is `╔`
- type 6 is `═`

Time to shape the street we promised!


## Input format

The first line contains three integers `S A B`, where `S` is the size of the grid, and `A` and `B` are the positions of the points to connect.
The second line contains `S` integers, the number of road parts expected in each column.
The third line contains `S` integers, the number of road parts expected in each row.
The following `S` lines contain `S` integers each, denoting a currently empty cell (`0`) or an existing road part that must be used as it is (`T`, with `T > 0`).


## Output format

`S` lines with `S` integers each, where each integer is either `0` if the cell is not used, or the type of road part to be built.


## Constraints

Instances are guaranteed to satisfy the following constraints:

* `S` does not exceed 15


## Example

Instance:

```
8 1 7
2 4 5 7 7 7 8 6
7 7 7 7 6 5 5 2
1 0 6 0 0 0 0 0
0 0 0 0 6 0 2 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 2 0 0 0
0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 5 0
```

Possible output:

```
1 5 6 6 6 6 1 0
4 3 5 6 6 1 2 0
0 5 3 5 1 2 4 1
0 4 1 2 2 4 6 3
0 0 4 3 2 5 6 1
0 0 0 5 3 4 1 2
0 0 0 4 6 6 3 2
0 0 0 0 0 0 5 3
```

Instances as the one above can be visualized on [ASP Chef](https://asp-chef.alviano.net/#eJylVtuWqjgQ/SUu2mfxqFyjgMMd8ibQQkJAz6ACfv1UULvtPv0ws+YpQCW7qnZVdvE+bU55txZLFb0hWlVOsJJTczEhzatceEZaUbnTaoE0XOR0fr5/IysRaVHlsPECZwakZZWj8nU1r4Dx8fywAeYaMFZf9s2rARjfv/2BgR7rTxj6v8SYV4h7RWx1w/LWvWIzPuyT5VCmHtl1/lQmUY9an2WS0uBYuZap/9XWbcDGBhygt0TuyT4BG0FyRqPB0fTJCQTZbb3JDr3Bpfo5oxvmqsLSCRl1E1w71BMz2nD/18KMpyz1T7m0AIyNl6WbGw7WWiRmd7vFbcsboqdfqHOFXF6RXYvr3HIZ2OvCWvfvEEdpbUQcDKSQ6ms5oTfcGn0hfcljKNq42SduXZoR93VIJTgvRZJrKAdEBoIT95iLypOTJpXca975LO+8V583nK7rojUgFsRxwkg3ND9A4EsRSwv6yPjD16O/NsohGH+hljWIHokbegsn8cZdWJ2dBA1YFQQc6ks70ReuhM5O64yYxu3O1IUsjCmPMZfXjPveJ8qFY0RSDLG4R6SLPOa+mOY4htJkELsDNetJIfvXQn3lxBgKc1wCp0LRxXNOe1OR4b3NkvHGedyb8QlLtQA+Jkdb8ZqLuRnfuM/cNICr4egEY4Eu25iJA9kGyyJvxzpr436roT5VbcKwUSDSXFJz2WcJ9Jpa3WxjIItTUqYqOtlwb55YrnrHatl3rOiB5X/Hkh5Y3hMLbN3W9BnkKeaWf7PV9SWXfJbK7jFL12xruWOZGBMOmh6Zy7nvgctmn8a3raYP22Co8nbulRZ6TtgCvhPi4V1dn+H9WsjrOpOgL8DfHCP4xFM9+9iqdWDrzolj4K46ehPwpnI/eLk10G+HrsC2erOD9aMXqtHW9D6aYI+Bqr+C1WiTZQgxa0gTQIMWl2jiPBTHOaagOkZk1LZz7A9u9OEE+z9jpfXPsYbHMzLZpbBi2If+dqZRsw2Pnw2QtgA9gLwfdYjV0bnz//Rb1zMvD3uqbtYz3+D3Xa2Ge74NxDbne9oRoXpoCfTHMNnGvTYfPJnz2UcN6wI1G15XztNiqzszTzP2nG8/Ame/QffAT/ONO6f3OHfPvIBL6Mfgh7pMuVz0EWmeMR+jVpGL6RX7Sw6f/BoZP0NzabwWpJb3JhOgd05Ie+ET4oC6JBzjJe/RNjbXUna+5q7WgDXwuJ85Dn/2y3/xjQDrB9866JblPO7EguvopUxEglPQK6rzu1zvU5eBVnzo5v28f8hS9wB6eQHNmLKEXUrLedW+BjTyfm+sDcMmo6DdjGtCKioEzjKX+od01qCYgqYccLKkPHdsKJT3KbwLHzoDh2zrc37g0G0c2ixcIpIs8Rs79OlOW52zVl9kRJBwmN12IRJx2MAsKX6aHxbc52Gv/i8NfL4fccK6vQWxUW+AO0Ie2gC8+KcyBVyKBtj3Xeu7j1nyOoc6l8Fso3v+j0HQ5/vMC68xfO8Yy82Rz69Xu4DTWphnkalMnGvuD3VfuFvuQj5HGN3BnN2F0Wjz2RKic5ZEoHfCuNOi0Wm9xU7DJINJ8gN34Zz/fcbM84X3x/u0uZWmMrzOBtDSIbeal/8ByFUuXvvkhTs0cwec9phzRhC9z+h1A/3AbAIzMRaVfwCFVEkk%21).

A visualization of the example output can also be inspected on [ASP Chef](https://asp-chef.alviano.net/#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%21).

Finally, we can take a look at the checker errors obtained for the malformed output 
```
1 5 6 6 6 6 1 0
4 3 5 0 6 1 2 0
0 5 3 5 1 2 4 1
0 4 1 2 2 4 6 3
0 0 4 3 2 5 6 1
0 0 0 5 3 4 1 2
0 0 0 4 6 6 3 2
0 0 0 0 0 0 5 3
```
on [ASP Chef](https://asp-chef.alviano.net/#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%21).

