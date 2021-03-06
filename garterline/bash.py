class BashPrompt(object):
    @staticmethod
    def attribute(attr):
        try:
            return Attributes[attr or "default"]["apply"]
        except KeyError as e:
            return attr
    @staticmethod
    def background(color):
        try:
            return BackgroundColor[color or "default"]
        except KeyError as e:
            return color
    @staticmethod
    def escape(sequence):
        try:
            return EscapeSequences[sequence or "escape"]
        except KeyError as e:
            return sequence
    @staticmethod
    def color(foreground="", background="", attribute=""):
        formats = []
        formats.append(BashPrompt.attribute(attribute))
        formats.append(BashPrompt.background(background))
        formats.append(BashPrompt.foreground(foreground))
        # "\[" + + "m\]"
        return BashPrompt.escape("") + "[" + ";".join(formats) + "m"
    @staticmethod
    def foreground(color):
        try:
            return ForegroundColor[color or "default"]
        except KeyError as e:
            return color

# TODO: All attribute test (hidden isnt logical)
Attributes = {
    "default": { "apply": "0", "reset": "0" },
    "blink": { "apply": "5", "reset": "25" },
    "bold": { "apply": "1", "reset": "21" },
    "dim": { "apply": "2", "reset": "22" },
    "hidden": { "apply": "8", "reset": "28" },
    "reverse": { "apply": "7", "reset": "27" },
    "underlined": { "apply": "4", "reset": "24" },
}

ForegroundColor = {
    "default": "39",
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "lightgray": "37",
    "gray": "90",
    "lightred": "91",
    "lightgreen": "92",
    "lightyellow": "93",
    "lightblue": "94",
    "lightmagenta": "95",
    "lightcyan": "96",
    "white": "97",
}

BackgroundColor = {
    "default": "49",
    "black": "40",
    "red": "41",
    "green": "42",
    "yellow": "43",
    "blue": "44",
    "magenta": "45",
    "cyan": "46",
    "lightgray": "47",
    "gray": "100",
    "lightred": "101",
    "lightgreen": "102",
    "lightyellow": "103",
    "lightblue": "104",
    "lightmagenta": "105",
    "lightcyan": "106",
    "white": "107",
}

EscapeSequences = {
    "escape": "\e", # an ASCII escape character (033)
    # SyntaxError: (unicode error) "unicodeescape" codec can"t decode bytes in position 0-1: truncated \uXXXX escape
    "username": "\\u", # the username of the current user
    "hostname": "\h", # the hostname up to the first `."
    "fullhostname": "\H", # the hostname
    "version": "\v", # the version of bash (e.g., 2.00)
    "fullversion": "\V", # the release of bash, version + patch level (e.g., 2.00.0)
    "terminal": "\l", # the basename of the shell"s terminal device name
    "directory": "\w", # the current working directory, with $HOME abbreviated with a tilde (uses the value of the PROMPT_DIRTRIM variable)
    "basedirectory": "\W", # the basename of the current working directory, with $HOME abbreviated with a tilde
    "time": "\@", # the current time in 12-hour am/pm format
    "fulltime": "\T", # the current time in 12-hour HH:MM:SS format
    "time24": "\A", # the current time in 24-hour HH:MM format
    "fulltime24": "\t", # the current time in 24-hour HH:MM:SS format
    "date": "\d", # the date in "Weekday Month Date" format (e.g., "Tue May 26")
    "fulldate": "\D", # the format is passed to strftime(3) and the result is inserted into the prompt string; an empty format results in a locale-specific time representation. The braces are required
    "jobs": "\j",# the number of jobs currently managed by the shell
    "shell": "\s",# the name of the shell, the basename of $0 (the portion following the final slash)
    "history": "\!",# the history number of this command
    "number": "\#",# the command number of this command
    "UID": "\$",# if the effective UID is 0, a #, otherwise a $
    "octal": "\nnn",# the character corresponding to the octal number nnn
    "begin": "\[",# begin a sequence of non-printing characters, which could be used to embed a terminal control sequence into the prompt
    "end": "\]",# end a sequence of non-printing characters
    "exitcode": "\$?",
    "bell": "\a", # an ASCII bell character (07)
    "newline": "\n",
    "return": "\r", # carriage return
}

# Cursor movement
# sc 	\E7 	save cursor position
# rc 	\E8 	restore saved cursor position
# clear 	\E[H\E[2J 	clear screen and move cursor to top left
# cuu #1 	\E[#1A 	move cursor up #1 rows
# cud #1 	\E[#1B 	move cursor down #1 rows
# cuf #1 	\E[#1C 	move cursor right #1 columns
# cub #1 	\E[#1D 	move cursor left #1 columns
# home 	\E[H 	move cursor to top left
# hpa #1 	\E[#1G 	move cursor to column #1
# vpa #1 	\E[#1d 	move cursor to row #1, first column
# cup #1 #2 	\E[#1;#2H 	move cursor to row #1, column #2

# Removing characters
# dch #1 	\E#1P 	remove #1 characters (like backspacing)
# dl #1 	\E#1M 	remove #1 lines
# ech #1 	\E#1X 	clear #1 characters (without moving cursor)
# ed 	\E[J 	clear to bottom of screen
# el 	\E[K 	clear to end of line
# el1 	\E[1K 	clear to beginning of line 
