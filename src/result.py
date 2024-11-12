from html import *

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

        name_text = font(self.name, color)
        resp_text = i(font(f'({str(self.responsible)})', 'indianred'))
        comm_text = i(font(f'({self.comment})', 'steelblue'))

        return name_text + '<br>' + resp_text + '<br>' + comm_text

# ==================================================================================================
