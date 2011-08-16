Name: basic256
Version: 0.9.6.66
Release: %mkrel 1
URL: http://kidbasic.sourceforge.net
Source: http://ovh.dl.sourceforge.net/sourceforge/kidbasic/basic256/%{name}_%{version}.tgz
Source1: basic256-0.9.6-doc.tar.gz
Source2: basic256.desktop
Source3: basic256_32.png
BuildRoot:	%{_tmppath}/%{name}%{version}-root
License: GPL
Group: Development/Other
BuildRequires: libqt4-devel libSDL-devel libSDL_mixer-devel sqlite3-devel gcc-c++ flex bison espeak libespeak-devel
Summary: Simple BASIC IDE that allows young children to learn to programming

%description
BASIC-256 is a simple BASIC IDE that allows young children to learn to program. 
It was written in response to David Brin's article, "Why Johnny Can't Code," 
in which he bemoans the lack of a simple, line-oriented programming language 
for children that runs on modern computers. It features a byte-code compiler 
and interpreter, a debugger, easy to use graphical and text output, and an editor.

%prep
%setup -q -c %{name}-%{version} -a1

%build
export CFLAGS="${RPM_OPT_FLAGS} -D_REENTRANT"
export CXXFLAGS="${RPM_OPT_FLAGS} -D_REENTRANT"
qmake
make %{?jobs:-j%jobs}
lrelease Translations/*.ts

%install
rm -rf %{buildroot}
mkdir -p %buildroot%_datadir/%name/Examples
mkdir -p %buildroot%_datadir/%name/help
install -D BASIC256 %buildroot%_bindir/BASIC256
install Translations/*.qm %buildroot%_datadir/%name/
install -D %SOURCE2 %buildroot%{_datadir}/applications//%name.desktop
install -D %SOURCE3 %buildroot%_iconsdir/%name.png
cp -r Examples %buildroot%_datadir/%name/
cp -r doc/en/ %buildroot%_datadir/%name/help/
cp -r doc/ru/ %buildroot%_datadir/%name/help/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CONTRIBUTORS license.txt ChangeLog
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/%name.desktop
%{_iconsdir}/%name.png

