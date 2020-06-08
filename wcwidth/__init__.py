"""
wcwidth module.

https://github.com/jquast/wcwidth
"""
# re-export all functions & definitions, even private ones, from top-level
# module path, to allow for 'from wcwidth import _private_func'.  Of course,
# user beware that any _private function may disappear or change signature at
# any future version.

# local
from .wcwidth import ZERO_WIDTH  # noqa
from .wcwidth import (WIDE_EASTASIAN,
                      wcwidth,
                      wcswidth,
                      _bisearch,
                      list_versions,
                      _wcmatch_version,
                      _wcversion_value)

# The __all__ attribute defines the items exported from statement,
# 'from wcwidth import *', but also to say, "This is the public API".
__all__ = ('wcwidth', 'wcswidth', 'list_versions')

# I used to use a _get_package_version() function to use the `pkg_resources'
# module to parse the package version from our version.json file, but this blew
# some folks up, or more particularly, just the `xonsh' shell.
#
# Yikes! I always wanted to like xonsh and tried it many times but issues like
# these always bit me, too, so I can sympathize -- this version is now manually
# kept in sync with version.json to help them out. Shucks, this variable is just
# for legacy, from the days before 'pip freeze' was a thing.
__version__ = '0.2.4'
