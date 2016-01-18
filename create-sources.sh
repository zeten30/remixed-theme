#!/bin/bash

#ICONS
cd icons
tar czf remixed-icon-theme.tar.gz Remixed
mv remixed-icon-theme.tar.gz ~/rpmbuild/SOURCES/

cd ..

#THEMES
cd themes
tar czf remixed-theme.tar.gz Remixed
mv remixed-theme.tar.gz ~/rpmbuild/SOURCES/


cd ..
