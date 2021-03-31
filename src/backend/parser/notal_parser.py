import ply.yacc as yacc
from src.backend.scanner.tmp_notal_scanner import TMPScanner

class NotalParser(object):
    tokens = TMPScanner.tokens
    start = 'expression'

    # grammar declaration here
    def p_relational_op(self, p):
        """relational_op : S_EQUAL
                | S_NOT_EQUAL
                | S_LESS_THAN_EQUAL
                | S_GREATER_THAN_EQUAL
                | S_LESS_THAN
                | S_GREATER_THAN
                | S_ELEMENT_OF
                | RW_EQ
                | RW_NEQ
        """

    def p_multiplicative_op(self, p):
        """multiplicative_op : S_TIMES
                            | S_DIVIDE
                            | RW_DIV
                            | RW_MOD
                            | RW_AND
        """

    def p_additive_op(self, p):
        """additive_op : S_PLUS
                    | S_MINUS
                    | RW_OR
                    | RW_XOR
        """

    def p_unary_op(self, p):
        """unary_op : S_PLUS
            |   S_MINUS
            |   RW_NOT
        """

    def p_expression(self, p):
        """expression : expression relational_op additive_expression
                    |   additive_expression
        """

    def p_additive_expression(self, p):
        """additive_expression : additive_expression additive_op multiplicative_expression
                            |   multiplicative_expression
        """

    def p_multiplicative_expression(self, p):
        """multiplicative_expression : multiplicative_expression multiplicative_op unary_expression
                                    |   unary_expression
        """

    def p_unary_expression(self, p):
        """unary_expression : unary_op unary_expression
                        |   primary_expression
        """

    # STILL NOT COMPLETE
    def p_primary_expression(self, p):
        """primary_expression : variable
                            | L_INTEGER_NUMBER
                            | L_STRING
                            | L_REAL_NUMBER
                            | L_BOOLEAN_TRUE
                            | L_BOOLEAN_FALSE
                            | L_CHARACTER
                            | S_LEFT_BRACKET expression S_RIGHT_BRACKET
        """

    # STILL NOT COMPLETE
    def p_variable(self, p):
        """variable : IDENTIFIER
        """

    # end of grammar declaration
    def p_error(self, p):
        print("Syntax error on input!")

    def __init__(self):
        self.lexer = TMPScanner()
        self.parser = yacc.yacc(module=self)

    def parse(self, source):
        self.source = source
        return self.parser.parse(source)