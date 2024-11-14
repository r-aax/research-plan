from thematic import Thematic
from html import *

# ==================================================================================================

class StateAssignmentYear:
    """
    State assignment in one year.
    """

# --------------------------------------------------------------------------------------------------

    def __init__(self, year):
        """
        Constructor.

        Parameters
        ----------
        year : int
            Year.
        """

        self.year = year

        # Empty thematics.
        self.thematics = []

# --------------------------------------------------------------------------------------------------

    def get_thematic_with_add_if_needed(self, name):
        """
        Get thematic (add new if there is no such thematic).

        Parameters
        ----------
        name : str
            Name of thematic.

        Returns
        -------
        Thematic
            Thematic.
        """

        for th in self.thematics:
            if th.name == name:
                return th

        assert False

# --------------------------------------------------------------------------------------------------

    def doctors(self):
        """
        Get doctors count.

        Returns
        -------
        int
            Doctors count.
        """

        return sum([t.doctors for t in self.thematics])

# --------------------------------------------------------------------------------------------------

    def candidates(self):
        """
        Get candidates count.

        Returns
        -------
        int
            Candidates count.
        """

        return sum([t.candidates for t in self.thematics])

# --------------------------------------------------------------------------------------------------

    def rids(self):
        """
        Get rids count.

        Returns
        -------
        int
            Rids count.
        """

        return sum([t.rids for t in self.thematics])

# --------------------------------------------------------------------------------------------------

    def publications(self):
        """
        Get publications count.

        Returns
        -------
        int
            Publications count.
        """

        return sum([t.publications for t in self.thematics])

# --------------------------------------------------------------------------------------------------

    def get_thematics_table_header_html(self):
        """
        Get HTML for table header.

        Returns
        -------
        str
            HTML code for table header.
        """

        # NB! we work with 3 thematics.
        assert len(self.thematics) == 3

        ths_html = ''.join([th(thematic.get_name_html(), '30%')
                            for thematic in self.thematics])

        return tr(f'<th width="10%">&nbsp;</th>{ths_html}')

# --------------------------------------------------------------------------------------------------

    def get_html(self):
        """
        Get HTML of table (one line of year, separated by thematics).

        Returns
        -------
        str
            HTML code.
        """

        header_tr = self.get_thematics_table_header_html()
        tds_html = ''.join([td(thematic.get_results_html()) for thematic in self.thematics])
        year_and_indicators_text = f'<b>{self.year}</b><br>{self.doctors()} doctors<br>'\
                                   f'{self.candidates()} candidates<br>{self.rids()} rids<br>'\
                                   f'{self.publications()} publications)'
        boody_tr = tr(f'{td(year_and_indicators_text)}{tds_html}')

        return table(f'{header_tr}{boody_tr}')

# ==================================================================================================
