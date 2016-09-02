from spack import *

class Bempp(Package):
    """BEM++ provides PDE Solving via the Boundary Element Method"""
    homepage = "http://www.bempp.org"
    url = "https://github.com/bempp/bempp"

    version("development", git = "https://github.com/bempp/bempp.git",
            branch="development")

    extends('python')

    depends_on("patchelf", type=("build", "link"))
    depends_on("tbb", type=("build", "link", "run"))
    depends_on("gmsh", type=("run"))
    depends_on("python@2.7.12:", type=("build","link","run"))
    depends_on("py-cython", type=("build","link","run"))
    depends_on("py-numpy", type=("build","link","run"))
    depends_on("py-scipy", type=("build","link","run"))
    depends_on("py-setuptools", type=("build","link","run"))
    depends_on("py-matplotlib", type=("build","link","run"))
    depends_on("boost", type=("build", "link", "run"))
    depends_on("eigen", type="build")
    #depends_on("paraview+python")
    

    parallel = True

    def install(self, spec, prefix):
        with working_dir('spack-build', create=True):
            cmake('..', *std_cmake_args)
            make()
            make('install')
