#!/usr/bin/env python
#
# lungct fs ChRIS plugin app
#
# (c) 2016-2020 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

from chrisapp.base import ChrisApp

import  os
from    os                      import listdir, sep
from    os.path                 import abspath, basename, isdir
from    distutils.dir_util      import copy_tree
import  shutil
import  pudb
import  sys
import  time
import  glob


Gstr_title = """


 _                        _
| |                      | |
| |_   _ _ __   __ _  ___| |_
| | | | | '_ \ / _` |/ __| __|
| | |_| | | | | (_| | (__| |_
|_|\__,_|_| |_|\__, |\___|\__|
                __/ |
               |___/

"""

Gstr_synopsis = """


    NAME

       lungct

    SYNOPSIS

        lungct                                                          \\
            [--dir <dir>]                                               \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <outputDir>

    BRIEF EXAMPLE

        * Bare bones execution

            mkdir out
            docker run --rm -u $(id -u)                                 \\
                -v  $(pwd)/out:/outgoing                                \\
                fnndsc/pl-lungct lungct                                 \\
                /outgoing

    DESCRIPTION

        `lungct` simply copies internal lungCT DICOM data dir to the
        <outputDir>. If an optional [--dir <dir>] is passed, then contents
        of <dir> are copied instead.

    ARGS

        [--dir <dir>]
        An optional override directory to copy to the <outputDir>.
        Note, if run from a containerized version, this will copy
        a directory from the *container* file system.

        [-h] [--help]
        If specified, show help message and exit.

        [--json]
        If specified, show json representation of app and exit.

        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.

        [--savejson <DIR>]
        If specified, save json representation file to DIR and exit.

        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.

        [--version]
        If specified, print version number and exit.

    EXAMPLES

    Copy the embedded lung CT data to the ``out`` directory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Here, files are copied as localuser
        mkdir out && chmod 777 out
        docker run --rm -u $(id -u)                                 \\
            -v  $(pwd)/out:/outgoing                                \\
            fnndsc/pl-lungct lungct                                 \\
            /outgoing

    Copy a user specified directory to the ``out`` directory
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Here, files are copied as root
        mkdir out && chmod 777 out
        docker run --rm                                             \\
            -v  $(pwd)/out:/outgoing                                \\
            fnndsc/pl-lungct lungct                                 \\
            --dir /etc                                              \\
            /outgoing

"""


class Lungct(ChrisApp):
    """
    This plugin simply copies a specific lung image of interest to its output directory.
    """
    PACKAGE                 = __package__
    CATEGORY                = ''
    TYPE                    = 'fs'
    ICON                    = '' # url of an icon image
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument('--dir',
                          dest          ='dir',
                          type          = str,
                          default       = '/usr/local/src/data/images',
                          optional      = True,
                          help          = 'directory override')

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())

        if len(options.dir):
            print("Copying tree %s..." % options.dir)
            copy_tree(options.dir, options.outputdir)
            sys.exit(0)
        else:
            print("No directory specified and no copy performed.")
            sys.exit(1)

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)


