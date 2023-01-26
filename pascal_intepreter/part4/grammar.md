> Write a grammar that describes arithmetic expressions containing any number of +, -, *, or / operators. With the
> grammar you should be able to derive expressions like “2 + 7 * 4”, “7 - 8 / 4”, “14 + 2 * 3 - 6 / 2”, and so on.

```
expr: term((PLUS | MINUS) term) *
term: factor((MUL | DIV) factor) *
factor: INTEGER
```