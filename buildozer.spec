[app]
title = The Silent Lantern
package.name = silentlantern
package.domain = org.echoes
source.dir = .
source.include_exts = py,json
version = 1.0
requirements = python3,pygame
orientation = landscape
fullscreen = 1
android.permissions = VIBRATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.allow_backup = True
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
