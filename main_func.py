#!/usr/bin/env python3
"""
"""

import os
from pathlib import Path
import sys

# Paths:{{{
relativetoprojectdir = '/'
__projectdir__ = Path(os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + relativetoprojectdir))
thisexternaldir = Path('/shared/cc_ra/test-mdc-call-external/')

# use a local version of the macrodata files rather than the standard version
uselocalmacrodata = True

# path to macrodata-code
mdc_local = Path(__projectdir__ / Path('submodules/macrodata-code/'))
macrodatacode_normal = Path('/home/a1cdc01/doc/research/macrodata-code/')

# path to macrodata-external
mde_local = thisexternaldir / Path('macrodata-external/')
macrodatapath_normal = Path('/shared/cc_ra/macrodata-external/')

if uselocalmacrodata is True:
    macrodatacode = mdc_local
    macrodatapath = mde_local
else:
    macrodatacode = macrodatacode_normal
    macrodatapath = macrodatapath_normal
# Paths:}}}

# always get functions to copy over macrodatacode/external from normal macrodatacode
sys.path.append(str(macrodatacode_normal / Path('codegen/setup-alt-folder/')))
from setup_alt_folder import *

# Macrodata:{{{1
def setupmacrodata(docopy = False):
    """
    Run setup of local macrodata.
    Can also do by running lines of code from setup_md_all here.
    """
    # all these paths are relative
    # merge datasets that I want to copy over to code/external
    # also copies over source folders associated with these (both to code and external folders)
    processdirs_input = ['process/investing-com/', 'process/cb-dates/']

    # processdirs skip - don't do these even if they're specified in processdirs_input or are modules that are called in processdirs_input
    processdirs_skip = []

    # other folders to copy over to code folder
    extracopy_mdc = []

    # other folders to copy over to external folder
    extracopy_mde = []

    # rsync over macrodata rather than copy
    mdrsync = True

    setup_md_all(mdc_local, mde_local, processdirs_input, processdirs_skip = processdirs_skip, extracopy_mdc = extracopy_mdc, extracopy_mde = extracopy_mde, mdrsync = mdrsync, docopy = docopy)


# Functions:{{{1
def full():
    setupmacrodata()


# Run:{{{1
if __name__ == "__main__":
    full()
