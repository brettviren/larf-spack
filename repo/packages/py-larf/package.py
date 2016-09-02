from spack import *

class PyLarf(Package):
    """LARF is a field calculation for wire time projection champers using BEM++."""

    homepage = "https://github.com/brettviren/larf"

    version("master", git = "https://github.com/brettviren/larf.git",
            branch="master")

    extends('python')

    depends_on('py-setuptools', type=('build','run'))
    depends_on('py-SQLAlchemy')

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
