Name:		remixed-theme
Version:	1.3
Release:	1
Summary:	Remix of my GTK2/3 themes
Group:		User Interface/Desktops
License:	GPL-3
URL:		https://github.com/zeten30/remixed-theme
Vendor:		Milan Zink <zeten30@gmail.com>
Source0:	remixed-theme.tar.gz
Requires: 	mozilla-fira-sans-fonts mozilla-fira-mono-fonts mozilla-fira-fonts-common gtk-murrine-engine gtk2-engines
BuildArch:	noarch

%description
Remixed-theme is a remix of my favourite GTK2/3 theme- Arc-Darker and customized default gnome-shell

%prep
%setup -q -n Remixed

%build
# Nothing to build

%install
%{__install} -d -m755 %{buildroot}%{_datadir}/themes/Remixed
for file in gtk-2.0 gtk-3.0 gnome-shell ; do
	%{__cp} -pr ${file} %{buildroot}%{_datadir}/themes/Remixed
done

%files
%defattr(-,root,root)
%doc CREDITS LICENSE.txt
%{_datadir}/themes/Remixed

%changelog
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
