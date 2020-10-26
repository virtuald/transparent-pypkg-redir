Transparent python package redirection demo
===========================================

A self-contained project to play around with redirecting python packages.

Scenario: `rootpkg.oldpkg.subpkg.mod` used to contain ClsInMod, but we decide 
`rootpkg.oldpkg` needs to be moved to `newpkg`. Can this be done without prior
users needing to change their code?

If the package is small or doesn't have submodules, it's straightforward to
just import everything and put it in sys.modules. However, if it's a lot of
things, I'd like to use python import hooks to do it. Turns out, you can!

Testing
-------

From bash, do `./run.sh` and it'll run all the experiments

Usage
-----

Do you think this would be useful in your own project? Repurpose this in your
own project by copying `rootpkg/oldpkg/__init__.py` and following the
instructions.

Requires Python 3.4+

Author/License
--------------

Dustin Spicuzza, MIT license