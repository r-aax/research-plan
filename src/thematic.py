from html import *

# ==================================================================================================

class Thematic:
    """
    Thematic.
    """

# --------------------------------------------------------------------------------------------------

    def __init__(self, name, year):
        """
        Constructor.

        Parameters
        ----------
        name : str
            Name.
        year : int
            Year.
        """

        self.name = name
        self.year = year

        # Empty results.
        self.results = []

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
