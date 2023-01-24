# Grammars

- specifies syntax of a language in a concise manner
- parser generator = program that accepts grammar as input and produces parser on output

Grammar example:

```
expr: factor((MUL | DIV) factor) *
factor: INTEGER
```

- consists of **rules (known as productions)**
- example has 2 rules
- rule consists of
    - **head** or **left-hand side** of the production
    - a colon
    - a sequence of **terminals** and/or **non-terminals** called **body** or right-hand side of the production
- in the example above:
    - terminals: `MUL`, `DIV`, `INTEGER`
    - non-terminals: `expr`, `factor`
- non-terminal on the LHS of the 1st rule is called the **start symbol**

> symbols: | -- or; () -- grouping of terminals/non-terminals, ()* -- zero or more times

- grammar defines a language