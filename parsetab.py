
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOX DIAMOND IMPLIES LPAREN NEGATION OR PREDICATE RPAREN\n    expression : LPAREN PREDICATE RPAREN\n    \n    expression : LPAREN NEGATION PREDICATE RPAREN\n               | LPAREN NEGATION expression RPAREN\n    \n    expression : LPAREN BOX PREDICATE RPAREN\n               | LPAREN BOX expression RPAREN\n               | LPAREN DIAMOND PREDICATE RPAREN\n               | LPAREN DIAMOND expression RPAREN\n    \n    expression : LPAREN expression IMPLIES expression RPAREN\n               | LPAREN expression AND expression RPAREN\n               | LPAREN expression OR expression RPAREN\n               | LPAREN PREDICATE IMPLIES expression RPAREN\n               | LPAREN PREDICATE AND expression RPAREN\n               | LPAREN PREDICATE OR expression RPAREN\n               | LPAREN expression IMPLIES PREDICATE RPAREN\n               | LPAREN expression AND PREDICATE RPAREN\n               | LPAREN expression OR PREDICATE RPAREN\n               | LPAREN PREDICATE IMPLIES PREDICATE RPAREN\n               | LPAREN PREDICATE AND PREDICATE RPAREN\n               | LPAREN PREDICATE OR PREDICATE RPAREN\n    '
    
_lr_action_items = {'LPAREN':([0,2,4,6,7,9,10,11,14,15,16,],[2,2,2,2,2,2,2,2,2,2,2,]),'$end':([1,8,27,28,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[0,-1,-2,-3,-4,-5,-6,-7,-17,-11,-18,-12,-19,-13,-8,-14,-9,-15,-10,-16,]),'PREDICATE':([2,4,6,7,9,10,11,14,15,16,],[3,12,17,19,21,23,25,30,32,34,]),'NEGATION':([2,],[4,]),'BOX':([2,],[6,]),'DIAMOND':([2,],[7,]),'RPAREN':([3,8,12,13,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[8,-1,27,28,35,36,37,38,39,40,41,42,43,44,-2,-3,45,46,47,48,49,50,-4,-5,-6,-7,-17,-11,-18,-12,-19,-13,-8,-14,-9,-15,-10,-16,]),'IMPLIES':([3,5,8,27,28,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[9,14,-1,-2,-3,-4,-5,-6,-7,-17,-11,-18,-12,-19,-13,-8,-14,-9,-15,-10,-16,]),'AND':([3,5,8,27,28,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[10,15,-1,-2,-3,-4,-5,-6,-7,-17,-11,-18,-12,-19,-13,-8,-14,-9,-15,-10,-16,]),'OR':([3,5,8,27,28,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,],[11,16,-1,-2,-3,-4,-5,-6,-7,-17,-11,-18,-12,-19,-13,-8,-14,-9,-15,-10,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,4,6,7,9,10,11,14,15,16,],[1,5,13,18,20,22,24,26,29,31,33,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> LPAREN PREDICATE RPAREN','expression',3,'p_expression_predicate','plyparser.py',39),
  ('expression -> LPAREN NEGATION PREDICATE RPAREN','expression',4,'p_expression_negation','plyparser.py',47),
  ('expression -> LPAREN NEGATION expression RPAREN','expression',4,'p_expression_negation','plyparser.py',48),
  ('expression -> LPAREN BOX PREDICATE RPAREN','expression',4,'p_expression_modal','plyparser.py',56),
  ('expression -> LPAREN BOX expression RPAREN','expression',4,'p_expression_modal','plyparser.py',57),
  ('expression -> LPAREN DIAMOND PREDICATE RPAREN','expression',4,'p_expression_modal','plyparser.py',58),
  ('expression -> LPAREN DIAMOND expression RPAREN','expression',4,'p_expression_modal','plyparser.py',59),
  ('expression -> LPAREN expression IMPLIES expression RPAREN','expression',5,'p_expression_propositional','plyparser.py',68),
  ('expression -> LPAREN expression AND expression RPAREN','expression',5,'p_expression_propositional','plyparser.py',69),
  ('expression -> LPAREN expression OR expression RPAREN','expression',5,'p_expression_propositional','plyparser.py',70),
  ('expression -> LPAREN PREDICATE IMPLIES expression RPAREN','expression',5,'p_expression_propositional','plyparser.py',71),
  ('expression -> LPAREN PREDICATE AND expression RPAREN','expression',5,'p_expression_propositional','plyparser.py',72),
  ('expression -> LPAREN PREDICATE OR expression RPAREN','expression',5,'p_expression_propositional','plyparser.py',73),
  ('expression -> LPAREN expression IMPLIES PREDICATE RPAREN','expression',5,'p_expression_propositional','plyparser.py',74),
  ('expression -> LPAREN expression AND PREDICATE RPAREN','expression',5,'p_expression_propositional','plyparser.py',75),
  ('expression -> LPAREN expression OR PREDICATE RPAREN','expression',5,'p_expression_propositional','plyparser.py',76),
  ('expression -> LPAREN PREDICATE IMPLIES PREDICATE RPAREN','expression',5,'p_expression_propositional','plyparser.py',77),
  ('expression -> LPAREN PREDICATE AND PREDICATE RPAREN','expression',5,'p_expression_propositional','plyparser.py',78),
  ('expression -> LPAREN PREDICATE OR PREDICATE RPAREN','expression',5,'p_expression_propositional','plyparser.py',79),
]
