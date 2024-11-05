# ==================================================================================================

class Result:
    """
    Result.
    """

# --------------------------------------------------------------------------------------------------

    def __init__(self, year, name, responsible, comment):
        """
        Constructor.

        Parameters
        ----------
        year : int
            Year of result.
        name : str
            Name of result.
        responsible : Person
            Responsible person.
        comment : str
            Comment string.
        """

        self.year = year
        self.name = name
        self.responsible = responsible
        self.comment = comment

# ==================================================================================================
