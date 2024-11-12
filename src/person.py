# ==================================================================================================

class Person:
    """
    Person.
    """

# --------------------------------------------------------------------------------------------------

    def __init__(self, name, position, table_number, year):
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
        year : int
            Birth year.
        """

        self.name = name
        self.position = position
        self.table_number = table_number
        self.year = year

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
