Name: basic256
Version: 0.9.6
Release: %mkrel 1
URL: http://kidbasic.sourceforge.net
Source: http://ovh.dl.sourceforge.net/sourceforge/kidbasic/%name-%version.tar.gz
Source1: basic256.desktop
Source2: basic256_32.png
Patch0: basic256-0.9.6-alt-fix-say-function.patch
BuildRoot:	%{_tmppath}/%{name}%{version}-root
License: GPL
Group: Development/Other
BuildRequires: qt4-devel SDL-devel SDL_mixer-devel sqlite3-devel gcc-c++ flex bison
Summary: Simple BASIC IDE that allows young children to learn to programming

%description
BASIC-256 is a simple BASIC IDE that allows young children to learn to program. 
It was written in response to David Brin's article, "Why Johnny Can't Code," 
in which he bemoans the lack of a simple, line-oriented programming language 
for children that runs on modern computers. It features a byte-code compiler 
and interpreter, a debugger, easy to use graphical and text output, and an editor.

%prep
%setup -q
cd trunk
%patch0 -p1

%build
cd trunk
export CFLAGS="${RPM_OPT_FLAGS} -D_REENTRANT"
export CXXFLAGS="${RPM_OPT_FLAGS} -D_REENTRANT"
qmake
make %{?jobs:-j%jobs}
lrelease Translations/*.ts

%install
rm -rf %{buildroot}
mkdir -p %buildroot%_datadir/%name/Examples
mkdir -p %buildroot%_datadir/%name/help
cd trunk
install -D BASIC256 %buildroot%_bindir/BASIC256
install Translations/*.qm %buildroot%_datadir/%name/
install -D %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -D %SOURCE2 %buildroot%_iconsdir/%name.png
cp -r Examples %buildroot%_datadir/%name/
cp -r ./../doc/en/ %buildroot%_datadir/%name/help/
cp -r ./../doc/ru/ %buildroot%_datadir/%name/help/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc trunk/CONTRIBUTORS trunk/license.txt trunk/ChangeLog
%{_bindir}/*
%{_datadir}/%name
%{_desktopdir}/%name.desktop
%{_iconsdir}/%name.png

