# Task 2 - Permissions - [Getting Started - Part 2] - (Mobile APK Analysis) Points: 50

## Intro

Using the extracted APK file, you're asked to reverse engineer the folder to find the SHA256 of the signing cert, the cert signer's name, and the app permissions.

I used [apktool](https://ibotpeaches.github.io/Apktool/) and ran `$ apktool d terrortime.apk` to decompile the APK. 

The AndroidManifest.XML file showed the app permissions. Since there wasn't a CERT.RSA in the /META-INF folder, finding the certs was a bit trickier.

I used [ripgrep](https://github.com/BurntSushi/ripgrep) to find that the issue may have been that the APK was signed using a V2 signing scheme, which means that there isn't a CERT.RSA file in /META-INF. Using [androguard](https://androguard.readthedocs.io/en/latest/intro/certificates.html) verified this.

I ran `$ androguard sign --all terrortime.apk` to retrieve the SHA256 hash for the signature. To get the common name (CN), I went into my Android SDK folder and ran `$ ./apksigner verify --print-certs ~/location/of/terrorTime.apk`, which reported the signer's certs.

## Flags

INTERNET

ACCESS_NETWORK_STATE

a03a8954b2880d24d379eeffc304413b8fc23554c5679e47a9802ee6173af7d9

dev_terrorTime_871015
