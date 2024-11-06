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

# --------------------------------------------------------------------------------------------------

    def get_html(self):
        """
        Get HTML for result.

        Returns
        -------
        str
            HTML code for result.
        """

        return self.name \
               + '<br><i><font color="indianred">(' + str(self.responsible) + ')</font></i>' \
               + '<br><i><font color="steelblue">(' + self.comment + ')</font></i>'

# ==================================================================================================
