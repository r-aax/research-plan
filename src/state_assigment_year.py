from thematic import Thematic

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

# ==================================================================================================
