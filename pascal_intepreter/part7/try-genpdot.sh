#!/bin/bash
python genptdot.py "(14 + 2) * 3 - 6 / 2" > \
  parsetree.dot && dot -Tpng -o parsetree.png parsetree.dot
