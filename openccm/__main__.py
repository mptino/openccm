########################################################################################################################
# Copyright 2024 the authors (see AUTHORS file for full list).
#
#                                                                                                                    #
# This file is part of OpenCCM.
#
#                                                                                                                    #
# shapelets is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public
#
# License as published by the Free Software Foundation, either version 2.1 of the License, or (at your option) any  later ver>
#                                                                                                                    #
# shapelets is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of>
#                                                                                                                     #
# You should have received a copy of the GNU Lesser General Public License along with shapelets. If not, see             #
# <https://www.gnu.org/licenses/>.                                                                                     #
########################################################################################################################

import sys

from .run import run

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("ERROR: Provide configuration file path.")
        exit(0)

    config_file_path = sys.argv[1]
    run(config_file_path)
