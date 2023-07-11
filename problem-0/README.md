# Problem 0

Your friend Giorgio Arcani is asking for your help, again!

He received a supply of buttons attached to patches, and now someone has to cut them out in order to complete some very expensive suits.
If that weren't enough, buttons in the same patch are also of mixed color, and therefore they must be properly separated after detaching.

Giorgio has no time to waste!
Find a way to detach buttons of the same color with a cut on cardinal directions or along diagonals.
A cut must involve at least two buttons, and all buttons along the cut are detached, so they must have the same color.

Given a patch with buttons, can you find a sequence of cuts that detaches all buttons?


## Input format

The first line contains two integers, the size `S` of the patch and the number `C` of colors.
The following `S` lines contain `S` integers each, denoting the color of the buttons (from `1` to `C`).


## Output format

A line with an integer `N` followed by `N` lines made of four integers `I1 J1 I2 J2`, representing a cut from `(I1,J1)` to `(I2,J2)`.


## Constraints

Instances are guaranteed to satisfy the following constraints:

* `S` between 5 and 7
* `C` between 5 and 6


## Example

Instance:

```
5 6
1 1 1 2 3
4 3 1 3 3
5 4 5 2 5
1 6 6 2 6
5 5 5 4 2
```

Possible output:

```
11
4 4 5 5
4 2 4 5
2 1 5 4
1 5 2 4
3 1 3 3
1 1 1 3
2 3 4 1
2 2 2 5
3 5 5 3
1 4 3 4
5 1 5 2
```

Instances as the one above can be yisualized on [ASP Chef](https://asp-chef.alviano.net/#eJy1VMmWozgQ/CUQpro59MEGg4WRGFYh3QyU2W2/h22Wr5+Eruop9/Rt3pxAmVIukRH5Ptm39LKTcx2/4ToqaDs+SLAdsbEvSLWdE2sjYYMUYJuxQbN0uaNvZWzggsbrXYQNvtxFcBfs4A+28AZXjm63aUefworPJ6YOeeJV7sWfchb1uPNbjrRGxNozT/xX38UGXzuIAL8xpa9ODHwVVngdDcTYTySQFNp5kxN6A633d17bLdUllYRtTZkoSe3JvG6W/M/Miiee+LcUbSCG7fHEnkWwMyKZ//QfFp864/r2DV+olCrbyu1EmR5oC/4yO+z6d6gjP9iyCIYqQ+Uzn/Cb6Mw+Qy99DFkXNydGy9yKllznBMF7FCFqamdcDZVg9JrK2icmTYLoM734bXrxvuacRbIrs86EWvASJ4z2puEHGHJpcn6AWZn/yvUxQ1s7B+M33LUNrq8VDb0NYd7ohsWdMDwIXZJEuFcdtt9QhO+kI6Oo48619hIP43qpMVV27ZL7xLTHEiNCMdRCr3gvLzX32bTWMeRWC7UTmFlfZYr/zPSvmJhDZo0qYCpll3jt6WRpCpw7zsZ5wfFkxTeBSglyTMTYLjOXUyuel5yAZw+9X0kwToJ5Nwc4+ctWjVV6iNtjoGYLjqmlTUeD9EKxW8E2L3epPj6hl4dA0as9GIFv9pBav9mr8QL31TU22MVUPlLkt0e95I7Z3I7BmKXVtkgtE2Y5XI9m0zO9uTnm+MD6rk4R5KtKw56aHrRQYEtsjmZRHKvtCD3eHH3XvQelwPq1IOF2OIJ+jsFujelWUvGhkSsL+tExi96DONhsir+q7eB8ie/syeWzxnVml/jOu3gC7EbAeuKsBQ6RL1prH9khlhJkzj85RyXoEzjjz19nAvOtl34TZQe4+zeOTGnRIG61M+/MWYRcSuTvq6456CBB8WPlPvPP8H3kVvzIf/EgfuUiimZhYNU1ONRqNgsX+VwMDrNL18J32kWIzM1EWaS64V75Exd9BfRkFf9Jt5/nL/xDK/86dd1TkK85JSsPJ6LDuwPwympr2CHtUoNY+R/XJ+v7q2aZOXFULHuq+udcnj+4tWhUFWyE/+zFD5htQM8fswWsYfeJ33Tsho1EwkYFvO7wL8P+k1zYgw4zW9JFdxIWMgntxjUKxDs8/VnHa///u3axAjtOyQphaQ8RbKpzIudn78ePvwFFLjS6%21).

An animated visualization of the example output can also be inspected on [ASP Chef](https://asp-chef.alviano.net/#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%21).

Finally, we can take a look at the checker errors obtained for the malformed output
```
12
4 4 6 6
4 2 4 5
2 1 5 4
1 5 2 4
3 1 3 3
1 2 1 3
2 3 4 1
2 1 2 5
3 5 5 3
3 4 5 2
1 4 5 1
```
on [ASP Chef](https://asp-chef.alviano.net/#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%21).


## Example solution (using ASP)

In folder [example-solution-using-asp](example-solution-using-asp), to be executed as follows:

```bash
$ ./run.sh <../instance.1.in
```
