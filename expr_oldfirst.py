#!/usr/bin/env python3

#
# Ensure that importing oldpkg first works fine
#

import sys

from rootpkg.oldpkg.subpkg.mod import ClsInMod as OldClsInMod
from newpkg.subpkg.mod import ClsInMod


assert ClsInMod is OldClsInMod
assert sys.modules["newpkg.subpkg.mod"] is sys.modules["rootpkg.oldpkg.subpkg.mod"]
assert sys.modules["newpkg.subpkg.mod"].__name__ == "newpkg.subpkg.mod"

print("OK")
