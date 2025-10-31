[app]
title = Calculator
package.name = simplecalculator
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
