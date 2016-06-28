Name:		remixed-theme
Version:	1.6
Release:	5%{?dist}
Summary:	Remix of Arc GTK2/3 themes
Group:		User Interface/Desktops
License:	GPL-3
URL:		https://github.com/zeten30/remixed-theme
Vendor:		Milan Zink <zeten30@gmail.com>
Source0:	remixed-theme.tar.gz
Requires: 	gtk-murrine-engine gtk2-engines adobe-source-sans-pro-fonts adobe-source-code-pro-fonts lato-fonts
BuildArch:	noarch

%description
Remixed-theme is a remix of my favourite GTK2/3 theme Arc-* and customized Arc gnome-shell theme

%prep
%setup -q -n themes

%build
# Nothing to build

%install
%{__install} -d -m755 %{buildroot}%{_datadir}/themes/
for file in Remixed Remixed-Light Remixed-Dark ; do
	%{__cp} -pr ${file} %{buildroot}%{_datadir}/themes
done

%files
%defattr(-,root,root)
%{_datadir}/themes/Remixed
%{_datadir}/themes/Remixed-Light
%{_datadir}/themes/Remixed-Dark

%changelog
* Wed Jun 28 2016 Milan Zink <zeten30@gmail.com> - 1.6-5
- Arc Theme updated
- Gnome-shell theme fonts resize

* Tue Jun 21 2016 Milan Zink <zeten30@gmail.com> - 1.6-4
- Arc Theme updated

* Thu Apr 7 2016 Milan Zink <zeten30@gmail.com> - 1.6-1
- Light / Dark variant added

* Fri Apr 1 2016 Milan Zink <zeten30@gmail.com> - 1.5-2
- Full theme set (including metacity, cinnamon, xfwm4)
- GTK2 uses dark theme

* Fri Apr 1 2016 Milan Zink <zeten30@gmail.com> - 1.5-1
- Full theme set (including metacity, cinnamon, xfwm4)
- Transparency dropped

* Tue Mar 29 2016 Milan Zink <zeten30@gmail.com> - 1.4-4
- GTK3/Gnome shell theme fixes

* Thu Feb 4 2016 Milan Zink <zeten30@gmail.com> - 1.4-3
- GTK3 theme fixes, package dependencies

* Thu Feb 4 2016 Milan Zink <zeten30@gmail.com> - 1.4-2
- Fonts in gnome-shell

* Mon Jan 18 2016 Milan Zink <zeten30@gmail.com> - 1.4-1
- GTK & gnome-shell theme update, rpmspec add '%dist'

* Fri Dec 4 2015 Milan Zink <zeten30@gmail.com> - 1.3-2
- GTK & gnome-shell theme update

* Wed Nov 11 2015 Milan Zink <zeten30@gmail.com> - 1.3-1
- master -> Fedora 23

* Mon Nov 9 2015 Milan Zink <zeten30@gmail.com> - 1.2-6
- Arc-Darker updates

* Tue Oct 13 2015 Milan Zink <zeten30@gmail.com> - 1.2-4
- Arc-Darker updates

* Thu Sep 17 2015 Milan Zink <zeten30@gmail.com> - 1.2-3
- Various RPM spec fixes

* Thu Sep 17 2015 Milan Zink <zeten30@gmail.com> - 1.2-2
- RPM spec dependencies

* Wed Sep 16 2015 Milan Zink <zeten30@gmail.com> - 1.2-1
- Unified colors GTK, Gnome-shell

* Tue Sep 15 2015 Milan Zink <zeten30@gmail.com> - 1.1-2
- Gnome-shell theme fixes

* Tue Sep 15 2015 Milan Zink <zeten30@gmail.com> - 1.1-1
- Gnome-shell theme changed

* Mon Sep 14 2015 Milan Zink <zeten30@gmail.com> - 1.0-2
- GTK2/3 updates

* Wed Sep 09 2015 Milan Zink <zeten30@gmail.com> - 1.0-1
- Initial package for Fedora
