[app]
# Title of your application
title = Simple Calculator

# Package name
package.name = simplecalculator

# Package domain (needed for android/apk)
package.domain = org.example

# Source code directory
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,kv,atlas

# Application version
version = 0.1

# Application requirements
requirements = python3,kivy

# Android specific
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.build_tools = 33.0.0

# Presplash and icon
presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png

# Orientation and display
orientation = portrait
fullscreen = 0

[buildozer]
# Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2
