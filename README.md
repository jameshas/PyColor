# PyColor
Easily print in color to the python console, on any platform, without external modules.

## Color Support
PyColor supports 16 colors.

| Color           | Trigger     |
|-----------------|-------------|
| Blue            | ^BLU        |
| Green           | ^GRN        |
| Cyan            | ^CYN        |
| Red             | ^RED        |
| Purple          | ^PUR        |
| Yellow          | ^YEL        |
| White (Default) | ^WHT        |
| Grey            | ^GRY        |
| Bright          | ^B[Trigger] |

*Note: Bright colors avaliable via B prefix. E.g: ^BGRN for Bright Green*

## Example Usage
PyColor is easy to use, simply import the module and create a PyColor object to use the print() method.
```python
import PyColor

String = "^REDThis text is red and could be used to show a ^YELcritical ^BREDerror"

# Colored Log
ColorfulLog = PyColor()
ColorfulLog.print(String)

# Standard Log (Color Markdown will be stripped before printing)
StdLog = PyColor(color=False)
StdLog.print(String)
```

## Platform Methods
PyColor is cross-platform and will determine the correct coloring method automatically.

#### Windows 10: ANSI via VTS
Windows 10 Anniversary edition added support for Virtual Terminal Sequences (VT100) allowing the use of ANSI escape characters.
#### Windows: SetConsoleTextAttribute
Earlier editions of Windows do not support ANSI / VT100 natively. Instead, api calls are made to `windll.kernel32.SetConsoleTextAttribute` with a `stdout flush` to support multi-colored lines.
#### Linux etc: ANSI Native
Platforms such as Linux support ANSI escape characters natively.
