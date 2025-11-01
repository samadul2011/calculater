[app]
title = Simple Calculator
package.name = simplecalculator
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy

presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.0

fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
