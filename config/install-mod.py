#!/usr/bin/env python
# This file is part of mctc-lib.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os import environ, listdir, makedirs
from os.path import join, isdir, exists
from sys import argv
from shutil import copy

build_dir = environ["MESON_BUILD_ROOT"]
if "MESON_INSTALL_DESTDIR_PREFIX" in environ:
    install_dir = environ["MESON_INSTALL_DESTDIR_PREFIX"]
else:
    install_dir = environ["MESON_INSTALL_PREFIX"]

include_dir = argv[1] if len(argv) > 1 else "include"
module_dir = join(install_dir, include_dir)

modules = []
for d in listdir(build_dir):
    bd = join(build_dir, d)
    if isdir(bd):
        for f in listdir(bd):
            if f.endswith(".mod"):
                modules.append(join(bd, f))

if not exists(module_dir):
    makedirs(module_dir)

for mod in modules:
    print("Installing", mod, "to", module_dir)
    copy(mod, module_dir)
