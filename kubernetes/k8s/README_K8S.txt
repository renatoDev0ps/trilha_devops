8a880f1b6145470e9dafddb714d06d30


#!/usr/bin/env bash

wget https://github.com/AdoptOpenJDK/openjdk15-binaries/releases/download/jdk-15%2B36/OpenJDK15U-jdk_x64_linux_hotspot_15_36.tar.gz
tar xvf OpenJDK15U-jdk_x64_linux_hotspot_15_36.tar.gz --directory /usr/lib/jvm/
update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-15+36/bin/java 4
update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-15+36/bin/javac 4
update-alternatives --config java
rm OpenJDK15U-jdk_x64_linux_hotspot_15_36.tar.gz