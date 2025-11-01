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
android.ndk = 25b
android.sdk = 33
android.allow_backup = False

[buildozer]
log_level = 2
