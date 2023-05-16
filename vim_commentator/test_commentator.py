"""Tests the commentator module."""

import os
import unittest

import commentator

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
TESTING_DIR = os.path.join(CURRENT_DIR, "test_files")


def readLines(root, file):
    """Used to load testing data reading them from the passed in file.

    Parameters:
    root (str): The root directory.
    file (str): The file to read.

    Returns:
    list[str]: The lines read from the file.
    """
    file = os.path.join(root, file)
    with open(file) as fin:
        return fin.readlines()


def getCommentChar(before_filename):
    """Retrieves the corresponding comment chars for the file passed. """
    f = before_filename.replace("before", "commentchar")
    f = os.path.join(TESTING_DIR, f)
    with open(f) as fin:
        for l in fin.readlines():
            return l.strip()


def getBeforeAfterFilenames():
    """Generate tuples of 'before', 'after' and commenting char.

    Yields:
    tuple[str, str, str]: A tuple of 'before', 'after' file names and the
    comment char.
    """
    files = sorted(os.listdir(TESTING_DIR))
    before = [f for f in files if f.startswith('before')]
    for f in before:
        comment_char = getCommentChar(f)
        yield f, f.replace("before", "after"), comment_char


def test_needsToCommentOut():
    """Tests the needsToCommentOut function."""
    lines = []
    assert not commentator.needsToCommentOut(lines)
    lines = ["def foo():", "     pass"]
    assert commentator.needsToCommentOut(lines)
    lines = ["def foo():", "#     pass"]
    assert commentator.needsToCommentOut(lines)
    lines = ["#def foo():", "#     pass"]
    assert not commentator.needsToCommentOut(lines)


def test_lenPrefixingSpaces():
    """Tests the lenPrefixingSpaces function."""
    assert 0 == commentator.lenPrefixingSpaces("")
    assert 0 == commentator.lenPrefixingSpaces("x = 1")
    assert 3 == commentator.lenPrefixingSpaces("   x = 1")


def test_findLeftMargin():
    """Tests the findLeftMargin function."""
    lines = []
    assert 0 == commentator.findLeftMargin(lines)
    lines = [
        "class X:",
        "    def foo():",
        "        pass",
    ]
    assert 0 == commentator.findLeftMargin(lines)
    lines = [
        "  class X:",
        "    def foo():",
        "        pass",
    ]
    assert 2 == commentator.findLeftMargin(lines)


def test_commentOut():
    """Tests the commentOut function."""
    line, expected = "x = 12", "# x = 12"
    retrieved = commentator.commentOut(line, 0)
    assert retrieved == expected

    line, expected = "        for l1, l2 in zip(expected, retrieved):", \
                     "    #     for l1, l2 in zip(expected, retrieved):"

    retrieved = commentator.commentOut(line, 4)
    print(retrieved)
    assert retrieved == expected


def test_uncommentOut():
    """Tests the uncommentOut function."""
    line, expected = "# def foo():\n", "def foo():\n"
    retrieved = commentator.uncommentOut(line)
    assert retrieved == expected

    line, expected = "# x = 12\n", "x = 12\n"
    retrieved = commentator.uncommentOut(line)
    assert retrieved == expected

    line, expected = "# #         x = Y.MY_NAME\n", "#         x = Y.MY_NAME\n"
    retrieved = commentator.uncommentOut(line)
    assert retrieved == expected

    line, expected = "# \n", "\n"
    retrieved = commentator.uncommentOut(line)
    assert retrieved == expected

    line, expected = "#             \n", "\n"
    retrieved = commentator.uncommentOut(line)
    assert retrieved == expected

    line, expected = " #             \n", "\n"
    retrieved = commentator.uncommentOut(line)
    assert retrieved == expected

    line, expected = "#     ##### x = Y.JUNK_AND_JUNK2\n", "    ##### x = Y.JUNK_AND_JUNK2\n"
    retrieved = commentator.uncommentOut(line)
    assert retrieved == expected


def test_toggleComments():
    """Tests the toggleComments function."""
    for f1, f2, commentOutChar in getBeforeAfterFilenames():
        print(f1)
        actual_lines = readLines(TESTING_DIR, f1)
        expected = readLines(TESTING_DIR, f2)
        retrieved = commentator.toggleComments(actual_lines, commentOutChar)
        assert len(expected) == len(retrieved)
        for l1, l2 in zip(expected, retrieved):
            assert l1 == l2


if __name__ == '__main__':
    unittest.main()
