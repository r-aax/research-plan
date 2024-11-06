# ==================================================================================================

class Person:
    """
    Person.
    """

# --------------------------------------------------------------------------------------------------

    def __init__(self, name, position, table_number):
        """
        Constructor.

        Parameters
        ----------
        name : str
            Name of person.
        position : str
            Position string.
        table_number : int
            Table number.
        """

        self.name = name
        self.position = position
        self.table_number = table_number

# --------------------------------------------------------------------------------------------------

    def __repr__(self):
        """
        Convert into string.

        Returns
        -------
        str
            String representation.
        """

        return f'{self.name}, {self.position}'

# ==================================================================================================
