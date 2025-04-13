#!/bin/bash

set -e

# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "This script must be run as root. Please use sudo." >&2
    exit 1
fi

if [ -d /tmp/archlive ]; then
	sudo rm -rfv /tmp/archlive
fi

# Check if the folder still exists
if [ -d /tmp/archlive ]; then
    echo "Error: The folder /tmp/archlive still exists. Exiting..."
    exit 1
else
	tput setaf 3
	echo "############################################################"
    echo "Folder /tmp/archlive successfully removed or not present."
	echo "############################################################"
	sleep 3
	tput sgr0
fi

echo "########################################################"
echo "########################################################"
echo "########################################################"
echo "########################################################"

packages_file="/tmp/archlive/packages.x86_64"

# Packages to add to the archiso profile packages
packages=(
	gcc
	git
	pkgconfig
	python
	python-pip
	python-build
	python-setuptools
	python-wheel
	python-simple-term-menu
	python-pyparted
	arcolinux-keyring
	arcolinux-mirrorlist-git
	arcoinstall-dev
	chaotic-keyring
	chaotic-mirrorlist
)

mkdir -p /tmp/archlive/airootfs/root/archinstall-git
cp -r . /tmp/archlive/airootfs/root/archinstall-git

cat <<- _EOF_ | tee /tmp/archlive/airootfs/root/.zprofile
	echo
	alias be="loadkeys be-latin1"
	alias arch="archinstall --advanced"
_EOF_

pacman --noconfirm -S archiso

cp -r /usr/share/archiso/configs/releng/* /tmp/archlive

sed -i /archinstall/d "$packages_file"

# Add packages to the archiso profile packages
for package in "${packages[@]}"; do
	echo "$package" >> "$packages_file"
done

cp pacman.conf /tmp/archlive
mkdir -p /tmp/archlive/work/x86_64/airootfs/etc/
cp pacman.conf /tmp/archlive/work/x86_64/airootfs/etc/

find /tmp/archlive
cd /tmp/archlive

mkarchiso -v -w work/ -o out/ ./

date=$(date +%Y.%m.%d)

cp /tmp/archlive/work/iso/arch/pkglist.x86_64.txt  /tmp/archlive/out/archlinux-$date-x86_64.iso.pkglist.txt
