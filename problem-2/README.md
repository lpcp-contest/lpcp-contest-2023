# Problem 2

Oops!
We got the math exercise :(

Luckily, it is a puzzle!

We are given 9 cells in a 3x3 grid, each cell containing a digit.
Our goal is to make all of them being 9.
To this aim, we can increment cells by an amount between 1 and 5 as many times we want.
As a side effect, every time we increment a cell, adjacent cells are also incremented by 1.
Two cells are adjacent if their row or column indices differ by 1.


## Input format

Nine lines, each one containing an integer being the initial value of a cell.
Cells are listed in the order left-to-right, top-to-bottom.


## Output format

Nine lines, each one containing a space-separated list of integers terminated by `0`.
Each list represents the increments on the corresponding cell (and can be empty).


## Constraints

Instances are guaranteed to satisfy the following constraints:

* Each of the nine lines in the input contains an integer that is at least `0` and at most `8`.


## Example

Instance:

```
7
4
4
6
5
4
0
7
6
```

Possible output:

```
1 0
3 0
1 0
0
0
1 1 2 0
4 5 0
0
0
```

Instances as the one above can be visualized on [ASP Chef](https://asp-chef.alviano.net/#eJy1VMm2ozYU/CUG87pZ9MIDYGEEMZOQdkY8M8p24gHE1+eC3clz0rucLHQsuQ63SnXr6lO6l/y0Uos1+kBNwfMmfC0GK33tV7AmjNbe2u1y4T+Ykx4PxOiLbF8Hp1AWJLkiEXZUM1uWmo8iC9+xkwtY17MIfRD9Wh8IYDXSaZP0eGNJHCm6L/bSi/e931g32ridv1YMHHeNT1iFm71Km3bif3AnlTQLL7m2gBrunmbuyKLVJlHpE99OmDGi5vINnXwl15d1IFiVb/0O8IpvV9dP0FFsXZVFfc216lFI9MGEfeXa2z16LtL2QPyqcJKJ65hp8L2WaL5tHlHd14z451w1f3rSZpr/yE9hl5/2XzlHlq0qLmzQgqY6cWLZmzBCwGWqxRb8t//F9eqLax6j4RsSXYuac+3H+wUm+yGIyxsmqGdrRWGxZXjEWvgaumGBB9akInAshcZpM2nM9VU3cR+IeZ9qJFoKWvwzstRJ85XLWUdfOB1ox9Cza8318MHXXz2xe+4MBniq8FM63+ngmDqcBSXDOPl4cNIL0yoFOCTeLKeeq7mTjhMnk1XLoI8FGRQu+zIXs79Qw4ZMVCPPJk3JxVuv7rkWdpnuVszpVC7LAa/bK3KMOXNMmPdiXXHUWArflmUOd8p1v6fE75jd17uovWeOwXPBzzNHVJ6TetjA/1CDLXYW/h03y4lHfEZVtGtQv4tAj2NDL/tzWrcXZA93tF5+eNHq1YOKehvrCtgV2aj8LVqedzb4H7WlJ5fjLlr+gQBHFn7DMrsvsWzLnVwOXgc1p16c0hsVqQRPBvBQUtJBNvCXGerufJsqmWaPzyz5CvQOdITjV6/Bi+bp00oyEl6oZivTbKHOPFJhjyymSqZ+n+eVQr4zLb3PmSbhEX7vhZPei7/6m75nTEtGtkFGsKGg1W6njNGx7D3iVoGDbr5INDy20ieJEcSW/quMhdA/7pT/aR5/nr/kaphzJZ5ZAL72kM35kngN323dDjLTwNvQPTM35TptDs7391kktqRaOb0/9d/navLl+ppPg5EB9vwNB88WMKfg+/DgNXgNbxr7x3wGcavguDXArxvsVXjXlADeN4/YHRbJDcelimO3DTalRgWSv57P+f7/+0wiHd4unZfMMe8sWtTHTC2O+x8//gSM6Rsc%21).

A visualization of the example output can also be inspected on [ASP Chef](https://asp-chef.alviano.net/#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%21).

Finally, we can take a look at the checker errors obtained for the malformed output 
```
1 0
4 0
0 1
6 0
0
1 1 4 0
4 5 0
0
0
```
on [ASP Chef](https://asp-chef.alviano.net/#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%21).

