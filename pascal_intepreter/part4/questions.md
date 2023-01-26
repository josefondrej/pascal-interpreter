```
expr: factor((MUL | DIV) factor) *
factor: INTEGER
```

1. What is a context-free grammar (grammar)?
    > way how to describe syntax of a language
1. How many rules / productions does the grammar have?
    > 2
1. What is a terminal? (Identify all terminals in the picture)
    > basic building blocks of the grammar, e.g. `MUL`, `DIV`, `INTEGER`
1. What is a non-terminal? (Identify all non-terminals in the picture)
    > compounds of terminals (and other non-terminals), e.g. `expr`, `factor`
1. What is a head of a rule? (Identify all heads / left-hand sides in the picture)
    > left hand side, e.g. `expr`, `factor`
1. What is a body of the rule? (Identify all bodies / right-hand sides in the picture)
    > right hand side, e.g. `factor((MUL | DIV) factor) *`, `INTEGER`
1. What is the start symbol of a grammar?
    > expr