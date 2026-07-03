"""Functions for determining whether a year is a leap year."""
def leap_year(year):
    """Return True if the year is a leap year."""
    if year % 4 == 0 :
        if year % 100 == 0 :
            return year % 400 == 0
        return True
    return False