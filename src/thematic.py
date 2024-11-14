from html import *

# ==================================================================================================

class Thematic:
    """
    Thematic.
    """

# --------------------------------------------------------------------------------------------------

    def __init__(self, name, year, percentage):
        """
        Constructor.

        Parameters
        ----------
        name : str
            Name.
        year : int
            Year.
        percentage : int
            Percentage of whole year money.
        """

        self.name = name
        self.year = year
        self.percentage = percentage

        # Empty results.
        self.results = []

# --------------------------------------------------------------------------------------------------

    def get_name_html(self):
        """
        Get name HTML.

        Returns
        -------
        str
            Name HTML.
        """

        return f'{self.name} (<i>{self.percentage}</i>%)'

# --------------------------------------------------------------------------------------------------

    def get_results_html(self):
        """
        Get results HTML, written in one table cell as numerated list.

        Returns
        -------
        str
            HTML code.
        """

        return ol(''.join([li(r.get_html()) for r in self.results]))

# ==================================================================================================
