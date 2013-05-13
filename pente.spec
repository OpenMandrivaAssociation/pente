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
BuildRequires: pkgconfig(x11) ncurses-devel
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


%changelog
* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.2.5-6mdv2010.0
+ Revision: 440527
- rebuild

* Mon Apr 06 2009 Funda Wang <fundawang@mandriva.org> 2.2.5-5mdv2009.1
+ Revision: 364390
- use correct icons

* Mon Apr 06 2009 Funda Wang <fundawang@mandriva.org> 2.2.5-4mdv2009.1
+ Revision: 364339
- rebuild

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.2.5-1mdv2008.1
+ Revision: 136656
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Fri Jul 13 2007 Adam Williamson <awilliamson@mandriva.org> 2.2.5-1mdv2008.0
+ Revision: 51696
- drop debian menu and X-Mandriva XDG menu category
- use fd.o icon spec
- use gamesbindir macro, don't hardcode /usr/games
- take better description from Debian (thanks)
- update BuildRequires
- bunzip2 patch
- revive package (requested by several users on forum)
- Import pente



* Wed Jul 11 2007 R. James  <rjames@mandriva.com> 2.2.5-1mdv2007.1
- updated to 2.2.5
- xdg menu with icons

* Thu Aug 23 2001 Lenny Cartier  <lenny@mandrakesoft.com> 2.2.2-2mdk
- rebuild

* Wed Jan 24 2001 Lenny Cartier  <lenny@mandrakesoft.com> 2.2.2-1mdk
- updated to 2.2.2

* Tue Sep 11 2000 Lenny Cartier  <lenny@mandrakesoft.com> 2.2.0-2mdk
- BM
- macros
- fix patch file 

* Mon Apr 10 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.2.0-1mdk
- clean spec
- bzip archives

* Fri Jan  1 1999 Andrea Borgia <borgia@students.cs.unibo.it>
- added "group" to .../wmconfig/pente

* Tue Nov 17 1998 Andrea Borgia <borgia@students.cs.unibo.it>
- changed email address
- used defattr

* Mon Jul 20 1998 Andrea Borgia <borgia@cs.unibo.it>
- updated spec file syntax

* Thu Feb 19 1998 Andrea Borgia <borgia@cs.unibo.it>
- added wmconfig entry

* Fri Jan 30 1998 Andrea Borgia <borgia@cs.unibo.it>
- rebuilt for glibc
