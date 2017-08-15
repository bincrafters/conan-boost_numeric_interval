from conans import ConanFile, tools, os

class BoostNumeric_IntervalConan(ConanFile):
    name = "Boost.Numeric_Interval"
    version = "1.64.0"
    url = "https://github.com/bincrafters/conan-boost-interval"
    source_url = "https://github.com/boostorg/interval"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["interval"]
    requires =  "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Detail/1.64.0@bincrafters/testing", \
                      "Boost.Logic/1.64.0@bincrafters/testing"

                      #config0 detail5 logic3

    def source(self):
        for lib_short_name in self.lib_short_names:
            self.run("git clone --depth=50 --branch=boost-{0} https://github.com/boostorg/{1}.git"
                     .format(self.version, lib_short_name)) 

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()