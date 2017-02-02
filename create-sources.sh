#!/bin/bash

#ICONS
cd icons
tar czf remixed-icon-theme.tar.gz Remixed
mv remixed-icon-theme.tar.gz ~/Projects/RH/rpmbuild/SOURCES/

cd ..

#THEMES
tar czf remixed-theme.tar.gz themes
mv remixed-theme.tar.gz ~/Projects/RH/rpmbuild/SOURCES/

#SPECS
cp *.spec  ~/Projects/RH/rpmbuild/SPECS/
