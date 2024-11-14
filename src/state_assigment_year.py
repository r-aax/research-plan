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

        new_th = Thematic(name, self.year)
        self.thematics.append(new_th)
        return new_th

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

        ths_html = ''.join([th(thematic.name, '30%') for thematic in self.thematics])

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
        boody_tr = tr(f'{td(b(self.year))}{tds_html}')

        return table(f'{header_tr}{boody_tr}')

# ==================================================================================================
