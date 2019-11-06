# Task 2 - Permissions - [Getting Started - Part 2] - (Mobile APK Analysis) Points: 50

## Intro

Using the extracted APK file, you're asked to reverse engineer the folder to find the SHA256 of the signing cert, the cert signer's name, and the app permissions.

I used [apktool](https://ibotpeaches.github.io/Apktool/) and ran `$ apktool d terrortime.apk` to decompile the APK. 

The AndroidManifest.XML file showed the app permissions. Since there wasn't a CERT.RSA in the /META-INF folder, finding the certs was a bit trickier.

I used [ripgrep](https://github.com/BurntSushi/ripgrep) to find that the issue may have been that the APK wasn't built and deployed in Android Studio. 

## Flags

INTERNET

ACCESS_NETWORK_STATE
