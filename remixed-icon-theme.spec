Name:		remixed-icon-theme
Version:	1.0
Release:	1
Summary:	Remix of my favourite icon themes
Group:		User Interface/Desktops
License:	GPL-3
URL:		https://github.com/zeten30/remixed-theme
Vendor:		Milan Zink <zeten30@gmail.com>
Source0:	remixed-icon-theme.tar.gz
BuildArch:	noarch

%description
Remixed-icon-theme is a remix of my icon themes Paper, Super Flat, Breeze

%prep
%setup -q -n Remixed

%build
# Nothing to build

%install
%{__install} -d -m755 %{buildroot}%{_datadir}/icons/Remixed
for file in actions apps categories cursors devices emblems emotes mimetypes places status index.theme ; do
	%{__cp} -pr ${file} %{buildroot}%{_datadir}/icons/Remixed
done

%files
%defattr(-,root,root)
%doc CREDITS LICENSE.txt
%{_datadir}/icons/Remixed

%changelog
* Wed Sep 09 2015 Milan Zink <zeten30@gmail.com> - 1.0-1
- Initial package for Fedora

