# buildozer.spec
[app]

# Mandatory fields
title = Calculator
package.name = calculator
package.domain = org.example   # change if you plan to publish
source.dir = .
source.include_exts = py,kv,png,jpg,atlas
version = 0.1

# Dependencies
requirements = python3,kivy==2.3.0

# UI options
orientation = portrait
fullscreen = 1
android.permissions = INTERNET

# (All other sections can stay at their defaults)
