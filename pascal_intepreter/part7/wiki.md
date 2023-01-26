- until now parser and interpreter code mixed -- interpreter evaluated expression as soon as parser recognized it --
  this is called **syntax directed interpreter**
- for more complex applications we need to build **immediate representation** (IR)
- **parse-tree** (concrete syntax tree) is a tree that represents syntactic structure of a language construct according
  to our grammar definition, example:
  ![img.png](img.png)
- **abstract syntax tree** represents abstract syntactic structure of a language construct ![img_1.png](img_1.png)
    - ASTs uses operators/operations as root and interior nodes and it uses operands as their children.
    - ASTs do not use interior nodes to represent a grammar rule, unlike the parse tree does.
    - ASTs don’t represent every detail from the real syntax (that’s why they’re called abstract) - no rule nodes and no
      parentheses, for example.
    - ASTs are dense compared to a parse tree for the same language construct.