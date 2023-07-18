# Problem 1

We have `S` exercises and `S` students.
We want to assign half of the exercises to every student, assigning different sets of exercises to different students.
To equaly assing exercises, we also want that every exercise is assigned to half of the students, where any two exercises should not be assigned to exactly the same set of students.

Moreover, the exercises and students are ordered. To guarantee a fair mix, any three consecutive exercises should neither be all assigned or all unassigned to the same student. Similarly, every exercise must be assigned to some and unassigned to another among three consecutive students.

Unfortunately, some of the exercises are already assigned to some students, and we also know that we cannot assign specific exercises to some students.
Can you help us for this assignment?

An instance of the problem is essentially a grid with some cells filled in with 0s and 1s.
A cell `(i,j)` is associated with `1` if the exercise `j` is assigned to the student `i`;
it is associated with `0` if the exercise `j` is not assigned to the student `j`.
Your task is to complete the grid.


## Input format

The first line contains one integer `S`, the size of the grid.
The following `S` lines contain `S` integers each, denoting an empty (`2`) or an already filled in cell (`0` or `1`).


## Output format

`S` lines with `S` integers each, where each integer is either `0` or `1`.


## Constraints

Instances are guaranteed to satisfy the following constraints:

* `S` is even
* `S` is at least 6
* `S` does not exceed 14


## Example

Instance:

```
6
1 2 2 0 2 2
2 2 0 0 2 1
2 0 0 2 2 1
2 2 2 2 2 2
0 0 2 1 2 2
2 1 2 2 0 0
```

Possible output:

```
1 0 1 0 1 0
0 1 0 0 1 1
1 0 0 1 0 1
0 1 1 0 1 0
0 0 1 1 0 1
1 1 0 1 0 0
```

Instances as the one above can be visualized on [ASP Chef](https://asp-chef.alviano.net/#eJy1VMm2okgQ/SUGeVUsaqEymEjCYYbcSfJkVrsVIfn6jkSt8nVXr/r0KofIiBvDzfvJrEt+2ojFFn2ghtC80UtcrxnS1suamivYoxJv1+OyxtMA9+PLjjQDfNBzj14+L/u03HWLz/S0c1ttb60u7507MePjIVHGIvVq9+SzIomuqPe7TFJbEqv3IvW/2k4W2LqRBOgjka/1IQFbjeSsiUas6QwHguz0HrNDb3Qa/ZY1VudsBQWHXeMkpMKNJ2ZNy/Hv1IxZlvqXXFpBDMvLUmsmwUaLxOxh33GbMqPm8g2dHCGX17XbkyrfOR3YK7rbXD8hj2JniSQYaypV94KhD9IbVyp9qWOkfdweEqcqzIhjHVMJ/KVIcgz1iOqxJolzzkX11ZM2lZx7fvK7/OS9Y84k3VS0NyAXxOOEkW5ofoAASxWLHczR+AfWc76Wegymb6jvWtScayf0VjjxJjcsbzhBI9kKAgl1xU70lSOhG+7xRJq4d01dyMK44Tnm8qbj2IdEHXiMSIohF+eMdJHnfKVsyWMszA5yxzCza01l/0637z0xRmpOCvRUoKd4qelgqjKc+yyZZt7HgxlfiFQJgMGwtuYzF3MznjkmYVVLYI5FMgmUjWXeL/2FGAZwopppynOKLvZ2M+SS36WyVRGzEykrJ7xtr8hUFs6RXh2KbUVRowt0V5Y51JTLzpglTkeMsd4HP2MLJK2EZR6myva74nxI/W4ftENqKjTv6Xl5F5TnqJ40uAcMstrr+A/crHke/WdQBfsGjWAr3Voon3w/42CcbAPzNwHShBIHqyGCmjy2VpGmD3aHOcZpv+QcnfcGunqs5e+bXJrutK7q3DSaA+OYU5X18XWv6Zd9eL4hsxvoLhbA508cTJoN9zb8Q+jf0pf9tgpsHV94ncDRK/DpTKBXn8F7rPW/xFovsRZOnOIbvGUwmwlmybKkA47it7/88E0lY35w2hGAQ8BJf36fOcykecxrw0jiXzLJEPgfR516zHpjJmEmpOL3RTcy+GepFA/L30r8I6xDYcZD8ZNn8VeuS9FMNKS4Wga5Gi3nejaXo51YlWuim9NHEp5b5iSR4oa6/Duu+9Abapb/SRde5zd+Cwu/+wcnAa89pAvPGd6C387qgLsNaFT34D7/X3FzML9/1YTEYJlUch2sf52r43OuXAMUkkywp1/s0LMV6MWTS9Br0FbyN51ww1bAYatAv26wF0FfBRd01k6MDvfRDYeliEOrdbVSynrEfq8TS/3/uzYgGTRUpiUx1YEEq/qYisXR+/HjL4F6YHI=%21).

A visualization of the example output can also be inspected on [ASP Chef](https://asp-chef.alviano.net/#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%21).

Finally, we can take a look at the checker errors obtained for the malformed output 
```
1 1 1 0 1 0
0 1 0 0 1 1
1 0 0 1 0 1
0 1 1 0 1 0
0 0 1 1 0 1
1 1 0 1 0 0
```
on [ASP Chef](https://asp-chef.alviano.net/#eJztWFmXssYW/UsM+t3lYyuCKFVeVMY3gVZmvKEV8NdnFw6Nwpes3DwkWStPLQV19hl2nbOrP5vlycunfDBTf1jNMvXz5cWPQm6/WKauOTl56aTxRL9cSfOSbKvrapucVcVs/GzSrBZB4wnj3BYp792+jT2hKkn0m9+09khrJz37C5O72xZW29Fxb42rwNYLElW1Js1PWjS9+3dsNEm9237sw3NTNW/7OE36eNtn9PbR6G1fw/DU7r5rH48wvOpt3zvetY9HGF7d3UdnPTyuxZt19+k9POzj+vve8fQ+3raHx/fjM3r5xL53PL6PZ/TySdv6veRF6Mfn9PHa+s3f9r3jOX28fv3EFu+FZ34fr+nFJ7Z4s9d9wGvr4Ikm1+Fs3VuLBtaa/hrq2LNHB+z1cVlMA2s9XPXJne5aH1cdwFWf/PleIwPxEoZb9dZ6uITh9vbSXhxkAFcfiFcfiFcfyLM+EK8+EK8+kGdjANcYiNcYwDUG4jUG4jUG4nUG8uwMxOsM5NkZwHUGcJ1HvJG9rSLXGqNvb1JbuPFdjU+ZY9VXl71TzPu7CR8sbnMiWCx59s7PzHhvT1N8731ijrh4p8YGt5bkhOySkbaTI6LoX1Qx6vWWD9dSEGm7ZUwsh3fjMKTKnHcatVSzSeXayzBQ0osXwUZKU8dexvvZlDJsb0EibYa5tNicMEuuwPuPmlPOEz+ideaG3oKmeB/6i2n5ue34J4SXoFF/uJlc+oIBnDDdW0HBYiDxR4U9TWDVqY9v1MwvEGvm2GYZLEipKuMLng+wEfqKUfiizMOndLWtjl42STAbG8fanAKbFGSHPjebnm95ci9erhf2TK3pYjpSFf6C76++IseutfHVKHnaDhRzFMhsZtZs5op7JeXcbXLS0vpsK+N81X5nFCtZLfUmYRjZ5yyUVrFaMT/cPCmMqGjQq06qVHy9ztN6x74xoo+JKs3PWoqY5uT43+1HrUXjHcNwm7D1eTULt9qcnNj3jjApPVEtnKwOHaFkmKVjLVNvdgSvkh/a9tEnw+3qOodfjG9j30P+2rxsj/CplvAt4qQXT4EGUILGsZOureontqrWVsQ4MeY9fOuDD6TlmnzyBZPVnvNzk9X7tleehD7Pcji+ou4h+jrnv9R8kyImVq8KfE32FgXPjGgdLQ+2AM4IhkDlyUGN2DmghcdPUi+jrD6JLcD/HPzL9SfPDjZXPrmeqby7m49orHOa5aZuRr6oZMa04cZrxeE1yxHozuCpdLw68TRyowGuJyw304Lhe+KU21uTM/MfGNdAmVTds4jvKm+RROt8A94ithz+iv73c4ffVGr5feOkuAxdJeWZXfAe+6YNuHhyBBl8a7nPzhfyFF66eMh36Ge0UOMiYv49ntu8oK5s/dMyS/wWX96Lm/RzsTncucRyDTw9es2dnFLLzWhGY22nj0hmoE8QYT3jQ3dHM80yKmrpI8ciFd6N6L994p/WJy6BvWk1FusHrab7HVsuePrZ9g3YzEzcOT5Oqx3z9zF72j2tNkPcnZ4TSq5Vl11b7KzDj+M64o7gTMPWPCu9+phxLvoF+x4+3/f9cVuuHXLoSeA4+D+rjnr7N3mpx33tuw+yO9WzBvf7EWoRgHd7azNk64/7JaQC5vlv+gU/wPd6+9Kjb77h2R2xvLcc2qIvtxx6xQjEJbgaHHzR/GKaAf0F9hiH3nCY7dnbLOjizMn/cL7uWMffx2F9h8XUvOfmWPiC/MXOmicGVw3nwIj8F2554BZspbfzcMRZIb/gbtDBf8SKc6vImAVVcbPxwbj8uBdfHYtP23hFnBPGR1nNb/G9n6m/h3/LZ50H/Hs9j7e9LMcL88vLCXyssb/tJ4/ecwHnz65gPGpWGE2J8972lltNZfXh870fhK2NF84vaOhZZjsfAovHvKuOq05OnndrdmeVyXvf+Kv9zFG/n/rZ78d+/qqFMN8E8xwo8/fa9f7not77HWy0eMyWKnH4Ozrj9ztWjlpL/wcWyxm01ojhSV1u4m+LZ0SjM34Db8Tm6xm5iFwbcz2eQ0tAc9m0nY2PeXrLC/qZTVnuzr64wQxEn8N87szhBHrrNjuZL0oaO/YmZZrC5ifQOjSl8eZgt3Mf9wxlcnjcU9x2Fo45PH/fVbBJW5TAhlaLVBEaIiFxMqIRH2H+JtpuE6+ljy8nm4+ciBPcnXNd75h+S8Zk5990A+oOH6AdRkyzLMChaj+76Y5Wc+TwPy8jxHPxZ129IFe+Uo872vS6Z5ro+7lwrTTfL+BbrFdkBq33qg2wrjKd8a5R86cu7eqT/KF7oEeYpnw8PzUC1vM09ZSa6Zrue47Nra5+Y3hq/pK7sWuR2hGgaxuuXu9oCH3GUegzB1ra3XIVuaaJY5kZkVC3HRnK3Q6zKnVE/Wh0aus3fyqX37r01Wbn/5bL4FVj0ti56jXuoAJiqFFz6HPjShpu5MZkrFmbzI1pSiQ3JYJe/+QuevFzHXNURv8ZM81c/nmtbk4OJj/5FRGyZXk=%21).

