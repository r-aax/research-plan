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

    def is_rid(self):
        """
        Check if it rid.

        Returns
        -------
        bool
            true - if result is rid,
            false - otherwise.
        """

        return self.name.startswith('База данных') or self.name.startswith('Программа для ЭВМ')

# --------------------------------------------------------------------------------------------------

    def get_html(self):
        """
        Get HTML for result.

        Returns
        -------
        str
            HTML code for result.
        """

        color = 'black'

        if self.is_rid():
            color = 'green'

        return '<font color="' + color + '">' + self.name + '</font>' \
               + '<br><i><font color="indianred">(' + str(self.responsible) + ')</font></i>' \
               + '<br><i><font color="steelblue">(' + self.comment + ')</font></i>'

# ==================================================================================================
