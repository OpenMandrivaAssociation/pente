%define name pente
%define version 2.2.5
%define release %mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Five in a row game for X
BuildRoot: %{_tmppath}/%{name}-buildroot
Source: %{name}-%{version}.tar.bz2
Source2: %name-icons.tar.bz2
Patch: pente-makefile.patch.bz2
Requires: x11-server-xorg
BuildRequires: XFree86-devel
Group: Games/Boards
License: GPL
URL: http://www.igoweb.org/~wms/comp/pente

%description
Five in a row game for X

%prep
rm -rf $RPM_BUILD_ROOT

%setup
%patch -p1

%build
%configure
%make

%install
mkdir -p $RPM_BUILD_ROOT/usr/games
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}{,/mini,/large}
%makeinstall
tar xvjf %{SOURCE2} 
cp %{name}-16.png $RPM_BUILD_ROOT/%_miconsdir/%name.png
cp %{name}-32.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
cp %{name}-48.png $RPM_BUILD_ROOT/%_liconsdir/%name.png

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%name <<EOF
?package(%name): \
 needs="x11" \
 section="More Applications/Games/Boards" \
 title="Pente" \
 longtitle="Five In a Row Game" \
 command="/usr/games/pente" \
 icon="pente.png" \
 xdg="true"
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Pente
Comment=Five In a Row Game
Exec=/usr/games/pente
Icon=pente.png
Terminal=false
Type=Application
Categories=GTK;X-MandrivaLinux-MoreApplications-Games-Boards;Game;BoardGame;
Encoding=UTF-8
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(,-, root, root)
%doc README
/usr/games/%name
%{_mandir}/man6/*
%{_menudir}/%name
%{_datadir}/applications/*.desktop
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png
