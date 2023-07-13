# Problem 4

Given a sequence of positive integers, repeately select a pair of integers and replace them with their absolute difference, until you are left with one integer.
What is the smallest integer you can obtain?


## Special evaluation rules

You will get 0 points if your solution provides a wrong answer in any tested instance (as usual).
Otherwise, you will get 1 point for each solved instance, unless another participant can provide a better solution than yours.

Stated differently, we don't strictly require to provide an optimal solution.
We will assign the point to the best solution we receive.


## Input format

One line with the initial integers.


## Output format

One line for each selected pair, each line containing the sequence of integers resulting after the above mentioned operation.
The order of integers in each sequence is not important.
Only one integer is expeceted in the last line.


## Constraints

Instances are guaranteed to satisfy the following constraints:

* The input consists of 6 or 7 integers.
* Each initial integer is at least 1 and at most 38.


## Example

Instance:

```
1 3 6 8 12 15
```

Possible output:

```
1 3 12 15 2
1 3 2 3
1 3 1
1 2
1
```

We can take a look at the checker errors obtained for the malformed output 
```
1 3 12 15 1
1 3 1 3
1 0 1
0 0
```
on [ASP Chef](https://asp-chef.alviano.net/#eJylVcuWqjoQ/SVA7bMY3IEiYhDiUpBHZhJsCCTqXbQG+PpbsVvbR/fgrDtMJeyq2rV3sevcY7af6LmF3uLO5XTvnikrmzTBmjddHT02ucW28Yh7U1vFvr4pWjg3flCfkMNPdB5pC3Vmsl8EwwLeyzxZHfxA9t40ffpu1Sytx+9wIFufPcWYbPEF39Tz+XPO+xhq/O455jd+iFTec56sr7VAX7au6ssGkXaf+zEGeD/Fvnp7iHWv77D1/M7/Ac9XePIl9oK3Ut/Kl9jLt+Mfcox/qHmschjPMah5+BK7zeTGq4RZAq8b4NXNPcvlmcBn4kTvX/NmS0HKbI453NUk/ry7YqLqqNF9pO46uDtSZ8OW/OMPErxG1YHhcDX041W7DIsPP0aSWJpGQnvkxfYQG+jDF35LqkgsHVtLw6hCTLJsABoVM20bmyeFsTGikgp8QLaucje0Qw0Spswdfs72PlvuG0YH6zMFzRMxa6ixgfuZpE47uquv3zrmAM4ijdueBJJtnehIjBJ6OHQ+cIP2rp45Ua9ykq6EXkmZx61GO1lkwqxJZALGTJKg7GmiagLOrMkpM9Y8GbglcbhOu6L1rbpBzujCExHmKbdKiiob+CqKDHrKBlimMeZkJtkCdJ84I5oJerjkCArQdOtCHDDIcGHX//rVWOURu6DoPrHbMhVRs7CHx0UwfvOCOx/adROyC+Z+calhc1jcZi2LDfsV+7BhDWjt8FuOm+cUhgdxj7cn4OnS/8Iqr/cNsmUTBLXCrTKjVbsGtLG64jzuH1uqdzfs0Ppr7DNo5USMzQv+Zef9hm9NXDQdFn4A3DOlp5GexbAvGXoDzzHAPFJDaeGmn0+OZ2ZJdRNyj/p87pbQA+jjXndrnhoXrUgqonob4zJXnmDue2K4Jbwx8Mx8VzoHvxwy3bz6rU4MDHpe82z/7bn3RGt2sNMJaBsJpIN3hrhaaV5MOBH+B55GFe600dJJdS9ODRxudDwt+rSaMMI+fUISt7x4BXpDdd6lyeTw5bOLx1T9kKPPHVPe+wPeyWxeg7/WXR5Db3uod0C/z6Lk2zg/qH8Nno4lcPTkBeCyUr6awPzXx9SYaSRQfVCm9kxqlOf7fPTqc/Cfqu96vvDimJ2K7+KoyZSP7+8Ha76br9+B9yaDG+Ba6Y09cFdxnvazKg2LgQf7xzds4G5lkEBnwD33wnG/jNcliVPpi4j73Q/cccxhP1S5NVl9zxY08n+4/N6t8gGzOmZIRB0V0DfXzfegve1UmHKFp7Yk0xR6mHHMNA2Hfu+FpfD7+oM4oAxjI7HY9GQ6+2Wnmh30MU3j0TkTvEpjqWZypvP1UWkb8v+BGrVsML6vsaTzSbODGYL29c+ZgTe7r3Oim0mi/fMfvinsnQ==%21).
