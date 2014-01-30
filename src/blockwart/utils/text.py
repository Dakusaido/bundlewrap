# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from os import environ
from random import choice
from string import digits, letters

from fabric import colors as _fabric_colors

VALID_NAME_CHARS = digits + letters + "-_.+"


def _ansi_wrapper(colorizer):
    if environ.get("BWCOLORS", "1") != "0":
        return colorizer
    else:
        return lambda s, **kwargs: s


def _bold_wrapper(text):
    return "\033[1m{}\033[0m".format(text)


bold = _ansi_wrapper(_bold_wrapper)
green = _ansi_wrapper(_fabric_colors.green)
red = _ansi_wrapper(_fabric_colors.red)
yellow = _ansi_wrapper(_fabric_colors.yellow)


def mark_for_translation(s):
    return s
_ = mark_for_translation


def randstr(length=24):
    """
    Returns a random alphanumeric string of the given length.
    """
    return ''.join(choice(letters + digits) for c in range(length))


def validate_name(name):
    """
    Checks whether the given string is a valid name for a node, group,
    or bundle.
    """
    try:
        for char in name:
            assert char in VALID_NAME_CHARS
        assert not name.startswith(".")
    except AssertionError:
        return False
    return True


def wrap_question(title, body, question):
    output = ("\n"
              " ╭  {}\n"
              " ┃\n".format(title))
    for line in body.splitlines():
        output += " ┃   {}\n".format(line)
    output += (" ┃\n"
               " ╰  " + question)
    return output
