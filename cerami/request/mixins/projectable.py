from ..search_attribute import (
    DictAttribute,
    ProjectionExpressionAttribute)
from ...datatype.expression import BaseExpression

class Projectable(object):
    """A mixin to add the project method"""

    def project(self, *datatypes_or_expressions):
        """return a new Request setup with project attributes

        Adds the ProjectionExpression, ExpressionAttributeNames to the
        request_attributes dict

        Arguments:
        datatypes -- a list of datatypes. List.index() and Map.key()
        can be passed to project specific nested attributes

        Returns:
        the instance of this class
        """
        for val in datatypes_or_expressions:
            names = {}
            if hasattr(val, 'expression_attribute_name'):
                expr = val
                names[expr.expression_attribute_name] = expr.datatype.column_name
            else:
                expr = BaseExpression('', val, None)
                names[expr.expression_attribute_name] = val.column_name
            self.add_attribute(
                ProjectionExpressionAttribute,
                'ProjectionExpression',
                expr)
            self.add_attribute(
                DictAttribute,
                'ExpressionAttributeNames',
                names)
        return self
