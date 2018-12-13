#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostNumeric_IntervalConan(base.BoostBaseConan):
    name = "boost_numeric_interval"
    url = "https://github.com/bincrafters/conan-boost_numeric_interval"
    lib_short_names = ["interval"]
    header_only_libs = ["interval"]
    b2_requires = [
        "boost_config",
        "boost_detail",
        "boost_logic"
    ]
