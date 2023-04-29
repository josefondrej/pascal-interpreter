## Basic pascal grammar

```
program: compound_statement DOT
compound_statement: BEGIN statement_list END
statement_list: statement | statement SEMI statement_list
statement: compound_statement | assignment_statement | empty
assignment_statement: variable ASSIGN expr
empty:
expr: term ((PLUS | MINUS) term)*
term: factor ((MUL | DIV) factor)*
factor: PLUS factor | MINUS factor | INTEGER | LPAREN expr RPAREN | variable
variable: ID
```

Symbol table (= the Interpreter.GLOBAL_SCORE in interpreter.py) is an abstract data type (ADT) for tracking
various symbols in source code.

## Hacks we have so far

- incomplete program definition
- variables have no declared types, no type checking (error on "3" + 5 etc.)
- a basic symbol table that also does double duty as a memory space
- using / instead of div keyword for integer division
