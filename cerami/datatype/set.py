from .base_datatype import DynamoDataType
from .mapper import SetMapperDecorator

class Set(DynamoDataType):
    """A class to represent a Set

    A set is a unique collection of primitive values. It can not be a collection of other
    Sets, Lists or Maps. They are represented in Cerami as arrays of values at the moment.

    Example:
    class Parent(db.Model):
        friends = Set(String())
    """
    def __init__(self, datatype, column_name="", default=None):
        """constructor for the Set

        The mapper and condition_type for the set is determined automatically
        by the datatype passed in.

        Arguments:
        datatype -- The primitive datatype of each item in the set
        column_name -- a string defining the name of the column on the table
        default -- a default value for the column. It can be a value or function
        """
        super(Set, self).__init__(column_name=column_name, default=default)
        self.datatype = datatype
        self.mapper = SetMapperDecorator(self.datatype.mapper)
        self.condition_type = self.datatype.condition_type + "S"
