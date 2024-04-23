import sympy
# sympy import symbols
from sympy.logic.boolalg import to_cnf
from sympy.abc import a, b, c, d, e
def clauses(expr) -> tuple:    # for DNFs only
    if not isinstance(expr, sympy.logic.boolalg.And):
        return expr,
    return expr.args

#a, b, c, d, e = symbols('a b c d e')

print(to_cnf( (b & ~a & ~e & c) | 
    (b & ~d & e & c) | 
    (~d & a & c & b) | 
    (~e & ~a & ~d & ~c) | 
    (~b & ~d & c & ~a) | 
    (~c & ~b & ~d & e) | 
    (~d & ~a & ~e & b) | 
    (b & ~e & ~c & ~a) | 
    (~b & ~e & ~c & a) | 
    (~d & ~c & b & ~e) | 
    (~c & ~b & ~a & ~d) | 
    (~b & d & a & c) | 
    (~e & ~c & a & ~d) | 
    (c & d & ~b & a) | 
    (~c & a & b & ~e) | 
    (~b & ~e & ~a & c) | 
    (a & ~e & ~b & ~c) | 
    (d & ~a & ~c & b) ))