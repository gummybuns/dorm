class SearchAttribute(object):
    """The base class for all attributes used for Request.add_attribute()

    Request has a request_attributes dict whose keys represent options for the request and
    values are different children of this base class. Request.build() iterates all of
    these attributes and calls this SearchAttribute.build().

    All Request methods return a reference to the caller, so it is possible to chain
    multiple methods of the same thing together.
    For example, Model.filter(Model.column1.eq(1)).filter(Model.column2.eq(2))

    The search attribute needs to decide how to handle duplicate calls. It may want
    to overwrite the first value, or do something to append them, That logic is
    handled by SearchAttribute.add()
    """

    def __init__(self, name, value=None):
        """constructor for the SearchAttribute

        Arguments:
        name -- a string representing the option for the Request.
            For example, for scanning it could be 'FilterExpression'

        Keyword Arguments
        value -- it can by anything - whatever should be associated with the name
        """
        self.name = name
        self.value = value

    def add(self, value):
        """setter for value

        All Request methods return a reference to the caller, so it is possible to chain
        multiple methods of the same thing together.
        For example, Model.filter(Model.column1.eq(1)).filter(Model.column2.eq(2))

        The search attribute needs to decide how to handle duplicate calls. It may want
        to overwrite the first value, or do something to append them, That logic is
        handled by SearchAttribute.add()
        """
        self.value = value

    def build(self):
        """build the SearchAttribute, which is called

        Request has a request_attributes dict whose keys represent options for the request
        and values are different children of this base class. Request.build() iterates all
        of these attributes and calls this SearchAttribute.build().

        Returns:
        the value
        """
        return self.value
