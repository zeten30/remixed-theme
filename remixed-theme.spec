Name:		remixed-theme
Version:	1.1
Release:	1
Summary:	Remix of my GTK2/3 themes
Group:		User Interface/Desktops
License:	GPL-3
URL:		https://github.com/zeten30/remixed-theme
Vendor:		Milan Zink <zeten30@gmail.com>
Source0:	remixed-theme.tar.gz
Requires: 	mozilla-fira-sans-fonts mozilla-fira-mono-fonts mozilla-fira-fonts-common
BuildArch:	noarch

%description
Remixed-theme is a remix of my favourite GTK2/3 theme- Arc-Darker and customized default gnome-shell

%prep
%setup -q -n Remixed

%build
# Nothing to build

%install
%{__install} -d -m755 %{buildroot}%{_datadir}/themes/Remixed
for file in gtk-2.0 gtk-3.0 gnome-shell images ; do
	%{__cp} -pr ${file} %{buildroot}%{_datadir}/themes/Remixed
done

%files
%defattr(-,root,root)
%doc CREDITS LICENSE.txt
%{_datadir}/themes/Remixed

%changelog
* Tue Sep 15 2015 Milan Zink <zeten30@gmail.com> - 1.1-1
- Gnome-shell theme changed

* Mon Sep 14 2015 Milan Zink <zeten30@gmail.com> - 1.0-2
- GTK2/3 updates

* Wed Sep 09 2015 Milan Zink <zeten30@gmail.com> - 1.0-1
- Initial package for Fedora
