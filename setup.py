# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Copyright: Red Hat Inc. 2013-2014
# Author: Lucas Meneghel Rodrigues <lmr@redhat.com>

import os

# pylint: disable=E0611
from setuptools import setup

VERSION = '0.30.0'

VIRTUAL_ENV = 'VIRTUAL_ENV' in os.environ


def get_dir(system_path=None, virtual_path=None):
    """
    Retrieve VIRTUAL_ENV friendly path
    :param system_path: Relative system path
    :param virtual_path: Overrides system_path for virtual_env only
    :return: VIRTUAL_ENV friendly path
    """
    if virtual_path is None:
        virtual_path = system_path
    if VIRTUAL_ENV:
        if virtual_path is None:
            virtual_path = []
        return os.path.join(*virtual_path)
    else:
        if system_path is None:
            system_path = []
        return os.path.join(*(['/'] + system_path))


def get_data_files():
    data_files = [(get_dir(['etc', 'avocado', 'conf.d']),
                   ['etc/avocado/conf.d/virt.conf'])]
    return data_files

setup(name='avocado-virt',
      version=VERSION,
      description='Avocado Virtualization Testing Plugin',
      author='Lucas Meneghel Rodrigues',
      author_email='lmr@redhat.com',
      url='http://github.com/avocado-framework/avocado-virt',
      packages=['avocado_virt',
                'avocado_virt.utils',
                'avocado_virt.qemu',
                'avocado_virt.plugins'],
      data_files=get_data_files()
      )
