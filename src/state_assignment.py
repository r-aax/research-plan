from state_assigment_year import StateAssignmentYear
from result import Result

# ==================================================================================================

class StateAssignment:
    """
    State assignment.
    """

# --------------------------------------------------------------------------------------------------

    def __init__(self, name, year_start, year_end):
        """
        Constructor.

        Parameters
        ----------
        name : str
            Name.
        year_start : int
            Start year.
        year_end : int
            End year.
        """

        assert year_end >= year_start

        self.name = name
        self.year_start = year_start
        self.year_end = year_end
        self.state_assignment_years = []
        self.set_years_interval(year_start, year_end)

# --------------------------------------------------------------------------------------------------

    def set_years_interval(self, year_start, year_end):
        """
        Set years interval.

        Parameters
        ----------
        year_start : int
            Start year.
        year_end : int
            End year.
        """

        self.state_assignment_years.clear()

        for year in range(year_start, year_end + 1):
            self.state_assignment_years.append(StateAssignmentYear(year))

# --------------------------------------------------------------------------------------------------

    def get_state_assignment_year(self, year):
        """
        Get state assignment of year.

        Parameters
        ----------
        year : int
            Year.

        Returns
        -------
        StateAssignmentYear
            State assignment of year.
        """

        assert (year >= self.year_start) and (year <= self.year_end)

        return self.state_assignment_years[year - self.year_start]

# --------------------------------------------------------------------------------------------------

    def add_result(self, year, thematic_name, name, responsible, comment):
        """
        Add result.

        Parameters
        ----------
        year : int
            Year.
        thematic_name : str
            Thematic name.
        name : str
            Result name.
        responsible : Person
            Responsible person.
        comment : str
            Comment string.
        """

        # Find year.
        assert (year >= self.year_start) and (year <= self.year_end)
        state_assignment_year = self.get_state_assignment_year(year)

        # Find thematic.
        thematic = state_assignment_year.get_thematic_with_add_if_needed(thematic_name)

        # Add result.
        thematic.results.append(Result(year, name, responsible, comment))

# --------------------------------------------------------------------------------------------------

    def print(self):
        """
        Print state assignment.
        """

        print(f'Theme: {self.name}')

        for say in self.state_assignment_years:

            print(f'\tYear: {say.year}')

            for thematic in say.thematics:

                print(f'\t\tThematic: {thematic.name}')

                for result in thematic.results:

                    print(f'\t\t\tResult: {result.name}')

# --------------------------------------------------------------------------------------------------

    def get_results_matrix_html(self):
        """
        Get HTML for results matrix.

        Returns
        -------
        str
            HTML code for results matrix.
        """

        h = '<html>'
        h = h + '<head><title>'
        h = h + self.name
        h = h + '</title></head>'
        h = h + '<body>'
        h = h + '<h2><center>' + self.name + '</center></h2>'
        h = h + '<table border="1">'
        h = h + '<tr><th width="10%">&nbsp;</th>'
        for thematic in self.state_assignment_years[0].thematics:
            h = h + '<th width="30%">' + thematic.name + '</th>'
        h = h + '</tr>'

        for say in self.state_assignment_years:

            h = h + '<tr><td><b>' + str(say.year) + '</b></td>'

            for thematic in say.thematics:

                h = h + '<td valign="top">'

                for result in thematic.results:

                    h = h + result.get_html() + '<br><br>'

                h = h + '</td>'

            h = h + '</tr>'

        h = h + '</table>'
        h = h + '</body></html>'
        return h

# ==================================================================================================
