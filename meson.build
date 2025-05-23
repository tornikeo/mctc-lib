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

project(
  'mctc-lib',
  'fortran',
  version: '0.3.0',
  license: 'Apache-2.0',
  meson_version: '>=0.55',
  default_options: [
    'buildtype=debugoptimized',
    'default_library=both',
  ],
)
install = not (meson.is_subproject() and get_option('default_library') == 'static')

# General configuration information
lib_deps = []
subdir('config')

# Collect source of the project
srcs = []
subdir('src')

# MCTC library target
mctc_lib = library(
  meson.project_name(),
  sources: srcs,
  version: meson.project_version(),
  include_directories: include_directories('include'),
  dependencies: lib_deps,
  fortran_args: [
    '-DWITH_JSON=@0@'.format(jsonfortran_dep.found() ? '1' : '0'),
  ],
  install: install,
)

# Export dependency for other projects and test suite
mctc_inc = mctc_lib.private_dir_include()
mctc_dep = declare_dependency(
  link_with: mctc_lib,
  include_directories: mctc_inc,
  dependencies: lib_deps,
)

# Add applications
subdir('app')

# Package the license files
mctc_lic = files(
  'LICENSE',
)

if install
  # Distribute the license files in share/licenses/<name>
  install_data(
    mctc_lic,
    install_dir: get_option('datadir')/'licenses'/meson.project_name()
  )

  module_id = meson.project_name() / fc_id + '-' + fc.version()
  meson.add_install_script(
    find_program(files('config'/'install-mod.py')),
    get_option('includedir') / module_id,
  )

  pkg = import('pkgconfig')
  pkg.generate(
    mctc_lib,
    description: 'Modular computation tool chain',
    subdirs: ['', module_id],
  )

  asciidoc = find_program('asciidoctor', required: false)
  if asciidoc.found()
    install_man(
      configure_file(
        command: [asciidoc, '-b', 'manpage', '@INPUT@', '-o', '@OUTPUT@'],
        input: files('man/mctc-convert.1.adoc'),
        output: '@BASENAME@',
      )
    )
  endif
endif

# add the testsuite
subdir('test')
