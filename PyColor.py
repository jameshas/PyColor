class PyColor():
    ''' A console logging class that supports colored text across all platforms.
    Methods:
        print: Print text to console
    '''

    # Required Import
    from datetime import datetime

    def __init__(self, color=True):
        # Make Color accessable outside __init__ scope
        self.color = color

        # Determine Correct Colorisation Method for the platform
        if self.color:
            from os import name
            from platform import release, version

            # Set method for colors
            self.colorMode = "ANSI"

            # Windows: Enable ANSI on Win10 otherwise use SetConsoleTextAttribute. All other platforms: ANSI
            if name == "nt" and release() == "10" and version() >= "10.0.14393":
                from ctypes import windll
                windll.kernel32.SetConsoleMode(windll.kernel32.GetStdHandle(-11), 7)    # Enable ANSI
            elif name == "nt":
                # Imports required for SetConsoleTextAttribute
                from sys import stdout
                from ctypes import windll
                from re import compile, search

                # Set Method for colors
                self.colorMode = "Windows"

                # Make Imports Avaliable outside Scope of Init
                self.stdout = stdout
                self.windll = windll
                self.compile, self.search = compile, search

        # Define ANSI and Int Colors for string replacement
        self.colors = (
            ("^BLU", "\033[0;34m", 1),      # Blue
            ("^GRN", "\033[0;32m", 2),      # Green
            ("^CYN", "\033[0;36m", 3),      # Cyan
            ("^RED", "\033[0;31m", 4),      # Red
            ("^PUR", "\033[0;35m", 5),      # Purple (Magenta)
            ("^YEL", "\033[0;33m", 6),      # Yellow
            ("^WHT", "\033[0;37m", 7),      # White (Standard)
            ("^BBLU", "\033[0;34;1m", 9),   # BRIGHT Blue
            ("^BGRN", "\033[0;32;1m", 10),  # BRIGHT Green
            ("^BCYN", "\033[0;36;1m", 11),  # BRIGHT Cyan
            ("^BRED", "\033[0;31;1m", 12),  # BRIGHT Red
            ("^BPUR", "\033[0;35;1m", 13),  # BRIGHT Purple (Magenta)
            ("^BYEL", "\033[0;33;1m", 14),  # BRIGHT Yellow
            ("^BWHT", "\033[0;37;1m", 15),  # BRIGHT White
            ("^GRY", "\033[0;37;2m", 8)     # Grey
        )

    def print(self, text):
        ''' Supports printing to console with color.
        Args:
            STRING text: String to print to console
        Returns:
            None
        '''

        if not self.color or self.colorMode == "ANSI":
            # Replace Color Key with ANSI Value or none for no color
            for k, vANSI, vWin in self.colors:
                text = text.replace(k, (vANSI if self.color else ""))

            # Print text to Console
            print(self.datetime.now().strftime("%H:%M:%S") + " | " + text)
        elif self.colorMode == "Windows":
            # Set stdoutHandle and setColor
            stdoutHandle = self.windll.kernel32.GetStdHandle(-11)
            setColor = self.windll.kernel32.SetConsoleTextAttribute

            # Print initial log
            print(self.datetime.now().strftime("%H:%M:%S") + " | ", end="")
            self.stdout.flush()

            # Loop through string searching for color markup
            searchKey = self.compile("(?P<colorTag>\\{})".format("|\\".join([x[0] for x in self.colors])))
            subCol = True
            while subCol:
                # Match First Instance of Color Markup in text
                subCol = searchKey.search(text)

                # Color Markup Found
                if subCol:
                    # subString Found
                    subString = text[:subCol.start()]

                    # Print valid subString
                    if len(subString):
                        print(subString, end="")
                        self.stdout.flush()

                    # Set Console color to subColor Found
                    subColor = subCol.group('colorTag')
                    setColor(stdoutHandle, self.colors[[x[0] for x in self.colors].index(subColor)][2])

                    # Remove subString from text and Continue
                    text = text[subCol.end():]

            # Print the remaining text
            print(text)
            self.stdout.flush()

            # Set Color to Default
            setColor(stdoutHandle, self.colors[6][2])
# End Log Class


# Logging
Log = PyColor()

Log.print("^BRED-- ^REDExample error string in red.")
Log.print("^BGRN++ ^GRNExample success string in green.")
Log.print("^WHT[] ^GRYExample info string in grey.")
Log.print("All Colours: ^BLUBlue, ^GRNGreen, ^CYNCyan, ^REDRed, ^PURPurple, ^YELYellow, ^WHTWhite, ^GRYGrey")
Log.print("All Colours: ^BBLUBlue, ^BGRNGreen, ^BCYNCyan, ^BREDRed, ^BPURPurple, ^BYELYellow, ^BWHTWhite ^WHT(Bright)")
