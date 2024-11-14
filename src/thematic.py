from html import *

# ==================================================================================================

class Thematic:
    """
    Thematic.
    """

# --------------------------------------------------------------------------------------------------

    def __init__(self, name, year, percentage, doctors, candidates, rids, publications):
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
        doctors : int
            Doctors count.
        candidates : int
            Candidates count.
        rid : int
            Result of intellectual actitivy count.
        publications : int
            Publications.
        """

        self.name = name
        self.year = year
        self.percentage = percentage
        self.doctors = doctors
        self.candidates = candidates
        self.rids = rids
        self.publications = publications

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

        return f'{self.name} (<i>{self.percentage}</i>%, '\
               f'{self.doctors} doctors, {self.candidates} candidates, '\
               f'{self.rids} rids, {self.publications} publications)'

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
