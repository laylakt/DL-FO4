import ply.lex as lex
import ply.yacc as yacc
import matplotlib.pyplot as plt
import numpy as np
import timeit


tokens = [
    'LPAREN',
    'RPAREN',
    'PREDICATE',
    'AND',
    'OR',
    'IMPLIES',
    'NEGATION',
    'BOX',
    'DIAMOND'
]


t_PREDICATE = r'[A-Z][a-z]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_AND = r'\&'
t_OR = r'\|'
t_IMPLIES = r'\->'
t_NEGATION = r'\~'
t_BOX = r'\[]'
t_DIAMOND = r'\<>'
t_ignore = r' '


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def p_error(p):
    print("Syntax error at '%s'" % p.value)


def p_expression_predicate(p):
    '''
    expression : LPAREN PREDICATE RPAREN
    '''
    p[0] = [p[2]]
    print(p[0])


def p_expression_negation(p):
    '''
    expression : LPAREN NEGATION PREDICATE RPAREN
               | LPAREN NEGATION expression RPAREN
    '''
    p[0] = [p[2], p[3]]
    print(p[0])


def p_expression_modal(p):
    '''
    expression : LPAREN BOX PREDICATE RPAREN
               | LPAREN BOX expression RPAREN
               | LPAREN DIAMOND PREDICATE RPAREN
               | LPAREN DIAMOND expression RPAREN
    '''

    p[0] = [p[2], p[3]]
    print(p[0])


def p_expression_propositional(p):
    '''
    expression : LPAREN expression IMPLIES expression RPAREN
               | LPAREN expression AND expression RPAREN
               | LPAREN expression OR expression RPAREN
               | LPAREN PREDICATE IMPLIES expression RPAREN
               | LPAREN PREDICATE AND expression RPAREN
               | LPAREN PREDICATE OR expression RPAREN
               | LPAREN expression IMPLIES PREDICATE RPAREN
               | LPAREN expression AND PREDICATE RPAREN
               | LPAREN expression OR PREDICATE RPAREN
               | LPAREN PREDICATE IMPLIES PREDICATE RPAREN
               | LPAREN PREDICATE AND PREDICATE RPAREN
               | LPAREN PREDICATE OR PREDICATE RPAREN
    '''
    p[0] = [p[3], p[2], p[4]]
    print(p[0])


lexer = lex.lex()
parser = yacc.yacc()


test = '((<>(<>P)) -> ([]((~P) | (Q))))'


print(test)
print()
x = parser.parse(test, lexer=lexer)


plt.rcParams['figure.figsize'] = [10, 6]
ns = np.linspace(1, 100, 1, dtype=int)
ts = timeit.timeit('x', 'from __main__ import x')
plt.plot(ns, ts, 'bo')
plt.show()
