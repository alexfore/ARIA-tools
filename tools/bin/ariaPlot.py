#! /usr/bin/env python3
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Author: Simran Sangha & David Bekaert
# Copyright (c) 2023, by the California Institute of Technology. ALL RIGHTS
# RESERVED. United States Government Sponsorship acknowledged.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Import functions
from ARIAtools.productPlot import cmdLineParse, main
from pkg_resources import get_distribution

if __name__ == '__main__':
    try:
        print('ARIA-tools Version:', get_distribution('ARIAtools').version)
    except BaseException:
        pass
    inps = cmdLineParse()
    main(inps)
