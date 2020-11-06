# TODO  Define the modules for use


class UICounter:
    """Interface class to keep UI-information"""
    bgcolor = "000000"
    fontcolor = "ffffff"


    # TODO  Create an init-method to load initial data from ini-file to app preferences
    def __init__(self, path):
        """Class Constructor"""

        def read_ini_file (path):
            """Read ini-data from file to dictionary"""
            # TODO write a code to read data from ini-file to dictionary


            pass

# TODO  Create an operation class to keep working info
class WorkProcess:
    """Operation class to keep working info"""

    def __init__(self):
        """Class Constructor"""
        pass


# TODO  Create an initial class to keep ini-information
class IniHub:
    """Class to keep ini-information"""

    def __init__(self):
        """Class Constructor"""
        pass


# TODO  Create an advertising class to manage adv_shows
class AdvertManager:
    """Class to manage advert shows"""

    def __init__(self):
        """Class Constructor"""
        pass


def main():
    print("hello, world!")


if __name__ == '__main__':
    main()
