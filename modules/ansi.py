# --------------------------------------
#            ANSI Color Codes
#        For Custom Print Colors
#      Use 'import ansi' for import
#    Use '{ansi.Color.RED}' for Colors
#   Use '{ansi.Format.BOLD}' to Format
#   Use '{ansi.Command.RESET}' to reset
# --------------------------------------

class Color:
    RED = "\033[31m"      # -| < Standard Status Colors for Command Line Interface
    GREEN = "\033[32m"    # -|
    YELLOW = "\033[33m"   # -|
    BLUE = "\033[34m"     # -|
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BLACK = "\033[30m"

class Format:
    BOLD = "\033[1m"      # -| < Standard Use Case for Errors
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"

class Command:
  RESET = "\033[0m"       # -| < Command to Reset Colors and Formats
