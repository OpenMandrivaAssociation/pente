%define debug_package %{nil}

Name:    pente
Version: 2.2.5
Release: 8
Summary: Five in a row game for X
Source:  http://www.igoweb.org/~wms/comp/pente/%{name}-%{version}.tar.gz
Source2: %{name}-icons.tar.bz2
Patch:   pente-makefile.patch
Group:   Games/Boards
License: GPL
URL:     http://www.igoweb.org/~wms/comp/pente
BuildRequires: pkgconfig(x11) 
BuildRequires: ncurses-devel

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
mkdir -p %{buildroot}/%{_gamesbindir}
mkdir -p %{buildroot}%{_mandir}/man6
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps

%makeinstall_std
tar xvjf %{SOURCE2} 
cp %{name}-16.png %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/%{name}.png
cp %{name}-32.png %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/%{name}.png
cp %{name}-48.png %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/%{name}.png
cp %{name}-32.png %{buildroot}/%{_iconsdir}/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Pente
Comment=Five in a row game
Comment[ru]=Игра "пять в ряд"
Exec=%{_gamesbindir}/pente
Icon=%{name}
Terminal=false
Type=Application
Categories=GTK;Game;BoardGame;
EOF

%files
%doc README
%{_gamesbindir}/%{name}
%{_mandir}/man6/*
%{_datadir}/applications/*.desktop
%_iconsdir/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
