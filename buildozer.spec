[app]
title = Simple Calculator
package.name = calculator
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.11.1
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21
android.arch = armeabi-v7a
android.accept_sdk_license = True
android.gradle_dependencies = org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.3.50
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
