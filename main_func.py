#!/usr/bin/env python3
"""
"""

import os
from pathlib import Path
import sys

relativetoprojectdir = '/'
__projectdir__ = Path(os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + relativetoprojectdir))
thisexternaldir = Path('/shared/cc_ra/test-mdc-call-external/')


# Macrodata:{{{1
# Macrodata Options:{{{1
# use a local version of the macrodata files rather than the standard version
uselocalmacrodata = True

# all these paths are relative
# merge datasets that I want to copy over to code/external
# also copies over source folders associated with these (both to code and external folders)
processdatasets = ['process/investing-com/', 'process/int-cb-policy/']

# other folders to copy over to code folder
extracopy_code = []

# other folders to copy over to external folder
extracopy_external = []

# rsync over macrodata rather than copy
mdrsync = True

# Macrodata Process Options:{{{1
# this section just processes the specified options
# probably don't need to change it

# path to macrodata-code
macrodatacode_this = Path(__projectdir__ / Path('submodules/macrodata-code/'))
macrodatacode_normal = Path('/home/a1cdc01/doc/research/macrodata-code/')

# path to macrodata-external
macrodatapath_this = thisexternaldir / Path('macrodata-external/')
macrodatapath_normal = Path('/shared/cc_ra/macrodata-external/')

if uselocalmacrodata is True:
    macrodatacode = macrodatacode_this
    macrodatapath = macrodatapath_this
else:
    macrodatacode = macrodatacode_normal
    macrodatapath = macrodatapath_normal

# always get functions to copy over macrodatacode/external from normal macrodatacode
sys.path.append(str(macrodatacode_normal / Path('codegen/setup-alt-folder/')))
from setup_alt_folder import *

def setupmacrodata():
    """
    This function sets up the necessary macrodata code to run everything locally
    Means I'm not using the overall macrodata-code/macrodata-external folders
    So can freeze code/data in place and not have it be affected by other projects
    """
    # this function copies across the macrodata-code
    copymdcode(processdatasets, macrodatacode_normal, macrodatacode_this, macrodatapath_this, extracopy_code = extracopy_code, rsync = mdrsync)

    # this function copies across any necessary files to macrodata-external
    copymdexternal(processdatasets, macrodatapath_normal, macrodatapath_this, extracopy_external = extracopy_external, rsync = mdrsync)

    # this function runs the process code
    runmdprocess(processdatasets)


