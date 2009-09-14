%define name pente
%define version 2.2.5
%define release %mkrel 6

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Five in a row game for X
BuildRoot: %{_tmppath}/%{name}-buildroot
Source: http://www.igoweb.org/~wms/comp/pente/%{name}-%{version}.tar.gz
Source2: %name-icons.tar.bz2
Patch: pente-makefile.patch
BuildRequires: libx11-devel ncurses-devel
Group: Games/Boards
License: GPL
URL: http://www.igoweb.org/~wms/comp/pente

%description
Pente is the English name for the Asian game ni-nuki, which itself 
is a version of the game go-moku. The game is a variant of the well 
known five in a row. Placing five stones in a row is one way to win, 
the other is to capture five pairs of the opponents stones.

Pente can run in three different modes: X, curses or text. You can 
play against the computer or another human, and there is also support 
for playing over a network. 

%prep
%setup -q
%patch -p1

%build
%configure2_5x --host=%{_host} --target=%{_target_platform} --with-x
%make CC="gcc %{optflags} %{?ldflags}"

%install
rm -fr %buildroot
mkdir -p $RPM_BUILD_ROOT/%{_gamesbindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
%makeinstall_std
tar xvjf %{SOURCE2} 
cp %{name}-16.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/16x16/apps/%name.png
cp %{name}-32.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/32x32/apps/%name.png
cp %{name}-48.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/48x48/apps/%name.png
cp %{name}-32.png $RPM_BUILD_ROOT/%_iconsdir/%name.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Pente
Comment=Five in a row game
Exec=%{_gamesbindir}/pente
Icon=%{name}
Terminal=false
Type=Application
Categories=GTK;Game;BoardGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%files
%defattr(,-, root, root)
%doc README
%{_gamesbindir}/%name
%{_mandir}/man6/*
%{_datadir}/applications/*.desktop
%_iconsdir/%name.png
%{_iconsdir}/hicolor/16x16/apps/%name.png
%{_iconsdir}/hicolor/32x32/apps/%name.png
%{_iconsdir}/hicolor/48x48/apps/%name.png
