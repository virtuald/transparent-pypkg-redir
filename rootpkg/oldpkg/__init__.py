#
# (C)2020 Dustin Spicuzza, MIT license
#
# To redirect your own modules:
#
# * Copy this file to your 'old' package as `__init__.py`
# * Change 'import newpkg' to 'import my_new_pkg as newpkg'
# * Everything else should 'just work'
#

import newpkg

import importlib
import importlib.util
import sys
import warnings


class LoaderWrapper:
    def __init__(self, name):
        self.name = name

    # Use deprecated load_module precisely because we *don't* want to
    # set the import-related attributes properly, as we're just passing
    # the other module through without modification
    #
    # TODO: file a bug to get this undeprecated or find a better way

    def load_module(self, fullname):
        sys.modules[fullname] = importlib.import_module(self.name)


class PackageFinder:

    oldpkg = __name__ + "."
    newpkg = newpkg.__name__ + "."

    @classmethod
    def find_spec(cls, fullname, path, target=None):
        if fullname.startswith(cls.oldpkg):
            newfullname = cls.newpkg + fullname[len(cls.oldpkg) :]
            loader = LoaderWrapper(newfullname)
            return importlib.util.spec_from_loader(fullname, loader)


warnings.warn(
    __name__ + " is deprecated, use " + newpkg.__name__ + " instead", DeprecationWarning
)

sys.meta_path.insert(0, PackageFinder)
sys.modules[__name__] = newpkg
del newpkg
