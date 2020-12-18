pl-lungct
================================

.. image:: https://travis-ci.org/FNNDSC/lungct.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/lungct

.. image:: https://img.shields.io/badge/python-3.8%2B-blue.svg
    :target: https://github.com/FNNDSC/pl-lungCT/blob/master/setup.py

.. contents:: Table of Contents


Abstract
--------

This plugin simply copies a specific lung image of interest to its output directory. This plugin is primarily of use in the COVID-NET workflow.


Description
-----------

``lungct`` simply copies internal lungCT DICOM data dir to the ``<outputDir>``. If an optional ``[--dir <dir>]`` is passed, then contents of ``<dir>`` are copied instead.


Usage
-----

.. code::

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

Arguments
~~~~~~~~~

.. code::

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


Getting inline help is:

.. code:: bash

    docker run --rm fnndsc/pl-lungct lungct --man


Development
-----------

Build the Docker container:

.. code:: bash

    docker build --build-arg UID=$UID -t local/pl-lungct .

Debug
-----

Assuming you are in the root dir of the source repo:

.. code:: bash

   docker run -ti                                                   \
    -v $(pwd)/lungct:/usr/local/lib/python3.8/dist-packages/lungct  \
    -v $(pwd)/out:/outgoing                                         \
    local/pl-lungct lungct /outgoing


Examples
--------

Copy the embedded lung CT data to the ``out`` directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need you need to specify input and output directories using the `-v` flag to `docker run`.


.. code:: bash

    # Here, files are copied as localuser
    mkdir out && chmod 777 out
    docker run --rm -u $(id -u)                                 \
        -v  $(pwd)/out:/outgoing                                \
        fnndsc/pl-lungct lungct                                 \
        /outgoing

Copy a user specified directory to the ``out`` directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    # Here, files are copied as root
    mkdir out && chmod 777 out
    docker run --rm                                             \
        -v  $(pwd)/out:/outgoing                                \
        fnndsc/pl-lungct lungct                                 \
        --dir /etc                                              \
        /outgoing


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
