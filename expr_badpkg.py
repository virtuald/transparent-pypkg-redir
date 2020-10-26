#!/usr/bin/env python3

try:
    from rootpkg.oldpkg import badpkg

    assert False, "badpkg didn't fail"
except ImportError:
    pass

try:
    from newpkg.oldpkg import badpkg

    assert False, "badpkg didn't fail"
except ImportError:
    pass

print("OK")
