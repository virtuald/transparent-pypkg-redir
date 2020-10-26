#!/usr/bin/env python3

#
# Ensure that importing newpkg first works fine
#

import sys

from newpkg.subpkg.mod import ClsInMod
from rootpkg.oldpkg.subpkg.mod import ClsInMod as OldClsInMod

assert ClsInMod is OldClsInMod
assert sys.modules["newpkg.subpkg.mod"] is sys.modules["rootpkg.oldpkg.subpkg.mod"]
assert sys.modules["newpkg.subpkg.mod"].__name__ == "newpkg.subpkg.mod"

print("OK")
