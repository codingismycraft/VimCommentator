"""Exposes functions for manipulating and toggling comments."""


def lenPrefixingSpaces(line):
    """Calculate the number of prefixing spaces in a line.

    Parameters:
    line (str): The line of text for which the prefixing spaces are counted.

    Returns:
    int: The number of prefixing spaces in the line.
    """
    if line == '\n':
        return 0
    else:
        return len(line) - len(line.lstrip())


def findLeftMargin(lines):
    """Find the minimum number of prefixing spaces among a list of lines.

    Parameters:
    lines (list[str]): A list of lines to search for the left margin.

    Returns:
    int: The minimum number of prefixing spaces among the lines.
    """

    return min(lenPrefixingSpaces(l) for l in lines) if lines else 0


def needsToCommentOut(lines, commentChar='#'):
    """Check if the passed in lines must be commented out or not.

    If at least one line is not a comment it will return True.

    Parameters:
    lines (list[str]): A list of lines to check for the need to comment.
    commentChar (str, optional): The comment character.

    Returns:
    bool: True if at least one line requires commenting, False otherwise.
    """
    return any(not line.lstrip().startswith(commentChar) for line in lines)


def commentOut(line, margin, commentChar='#'):
    """Comment out a line with a specified margin and comment character.

    Parameters:
    line (str): The line to be commented out.
    margin (int): The desired left margin.
    commentChar (str): The comment character.

    Returns:
    str: The commented line with the specified margin and comment character.
    """
    left_over = lenPrefixingSpaces(line) - margin
    if line == '\n':
        return commentChar + "\n"
    else:
        return margin * ' ' + \
               commentChar + ' ' + ' ' * left_over + line.lstrip()


def uncommentOut(line, commentChar='#'):
    """Uncomments out a line.

    Parameters:
    line (str): The line to be uncommented out.
    commentChar (str): The comment character.

    Returns:
    str: The uncommented line.
    """
    x = lenPrefixingSpaces(line)
    l = len(commentChar)
    assert line[x:x + l] == commentChar
    prefix, suffix = line[0:x], line[x + l:]
    return prefix + suffix[1:] if len(suffix.strip()) > 0 else "\n"


def toggleComments(lines, commentChar='#'):
    """Toggle comments in a list of lines based on a specified comment character.

    Parameters:
    lines (list[str]): A list of lines to toggle comments on.
    commentChar (str, optional): The comment character.

    Returns:
    list[str]: The modified list of lines with comments toggled.
    """
    if needsToCommentOut(lines, commentChar):
        m = findLeftMargin(lines)
        return [commentOut(l, m, commentChar) for l in lines]
    else:
        return [uncommentOut(l, commentChar) for l in lines]
