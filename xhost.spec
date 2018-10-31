Name: xhost
Version: 1.0.7
Release: 5
Summary: Server access control program for X
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Patch0: xhost-1.0.6-compile.patch
License: MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xau) >= 1.0.0
BuildRequires: pkgconfig(xmu) >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: setup < 2.7.10

%description
The xhost program is used to add and delete host names or user names to the
list allowed to make connections to the X server. In the case of hosts, this
provides a rudimentary form of privacy control and security. It is only
sufficient for a workstation (single user) environment, although it does limit
the worst abuses. Environments which require more sophisticated measures should
implement the user-based mechanism or use the hooks in the protocol for passing
other authentication data to the server.

%prep
%setup -q
%apply_patches

%build
autoreconf -fi
%configure
%make

%install
%makeinstall_std

%files
%{_bindir}/xhost
%{_mandir}/man1/xhost.1%{_extension}
