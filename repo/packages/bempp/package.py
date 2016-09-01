from spack import *

class Bempp(Package):
    """BEM++ provides PDE Solving via the Boundary Element Method"""
    homepage = "http://www.bempp.org"
    url = "https://github.com/bempp/bempp"

    version("development", git = "https://github.com/bempp/bempp.git",
            branch="development")

    
    depends_on("cmake@3.6.1:", type="build")
    depends_on("tbb")
    depends_on("gmsh")
    depends_on("python@2.7.12:")
    depends_on("py-cython")
    depends_on("py-numpy")
    depends_on("py-scipy")
    depends_on("py-setuptools")
    depends_on("py-matplotlib")
    #depends_on("paraview+python")
    

    parallel = True

    def install(self, spec, prefix):
        with working_dir('spack-build', create=True):
            cmake('..', *std_cmake_args)
            make()
            make('install')
