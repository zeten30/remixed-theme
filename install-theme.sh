#!/bin/bash

# !!! Only temporary solution - will built RPM's

#Remove old stuff
sudo rm -rf /usr/share/themes/Remixed /usr/share/icons/Remixed
#Create theme dirs
sudo mkdir -p /usr/share/themes/Remixed /usr/share/icons/Remixed

#Copy files
sudo cp -rf icons/Remixed/* /usr/share/icons/Remixed/
sudo cp -rf themes/Remixed/* /usr/share/themes/Remixed/
