Name: xhost
Version: 1.0.5
Release: 1
Summary: Server access control program for X
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxau-devel >= 1.0.0
BuildRequires: libxmu-devel >= 1.0.0
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

%build
%configure2_5x
%make

%install
%makeinstall_std


%files
%{_bindir}/xhost
%{_mandir}/man1/xhost.1%{_extension}
