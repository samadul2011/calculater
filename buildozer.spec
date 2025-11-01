[app]
# Title of your application
title = Calculator

# Package name
package.name = calculator

# Package domain (needed for android/ios packaging)
package.domain = org.example

# Source code where the main.py live
source.dir = .

# Source files to include (let's assume you have main.py and .kv files)
source.include_exts = py,png,jpg,kv,atlas

# Version of your application
version = 0.1

# Application requirements
# kivy version should match your requirements.txt
requirements = python3,kivy==2.3.0

# Supported orientations
orientation = portrait

# Fullscreen mode
fullscreen = 1

# Android specific
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True

# iOS specific (not needed for Android builds but included for completeness)
ios.kivy_ios_branch = master
ios.ios_deploy_branch = 1.10.0

# Skip the compilation of .py to .pyc
android.skip_update = False
android.accept_sdk_license = True

[buildozer]
# Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# Display warning if buildozer is run as root
warn_on_root = 0
