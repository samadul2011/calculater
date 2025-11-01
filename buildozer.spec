[app]
title = Simple Calculator
package.name = simplecalculator
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy

# Android specific
android.api = 33
android.minapi = 21
android.ndk = 25.1.8937393
android.sdk = 33
android.build_tools = 33.0.0

# Presplash and icon
presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
