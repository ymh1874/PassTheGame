# props/

Drop your image files here.  The game loads them automatically if they exist;
otherwise it falls back to the built-in drawn versions.

| Filename    | Used by   | Recommended size | Notes                              |
|-------------|-----------|------------------|------------------------------------|
| cloud.png   | cloud.py  | 160 × 80 px      | PNG with transparency (RGBA)       |
| sun.png     | sun.py    | 150 × 150 px     | PNG with transparency (RGBA)       |
| carrot_icon.png  | game.py | 64 × 64 px     | Square PNG, mature plant icon      |
| lettuce_icon.png | game.py | 64 × 64 px     | Square PNG, mature plant icon      |
| tomato_icon.png  | game.py | 64 × 64 px     | Square PNG, mature plant icon      |

All images should be **PNG with an alpha channel** so transparency works
correctly against the sky background.

If a seed icon is missing, the UI falls back to a letter placeholder.

*Note: There are no real rules as long as your code works*

Future contributors: add your own prop filenames to this table when you
introduce new sprites.
