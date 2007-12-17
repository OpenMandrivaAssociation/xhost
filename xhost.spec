Name: xhost
Version: 1.0.2
Release: %mkrel 3
Summary: Server access control program for X
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
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
rm -rf %{buildroot}
%makeinstall_std

install -d -m 755 %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/20xhost.csh <<EOF
# Export Xauthority for users not for root.

if ($?DISPLAY) then
    if (! $?SSH_TTY) then
        if ( `id -u` >= 14 ) then
            if (! $?XAUTHORITY) then
                setenv XAUTHORITY $HOME/.Xauthority
            endif
        endif
    endif
endif
EOF

cat > %{buildroot}%{_sysconfdir}/profile.d/20xhost.sh <<EOF
# Export Xauthority for users not for root.

if [ ! -z "$DISPLAY" -a -z "$SSH_TTY" ];then
    if [ "`id -u`" -gt 14 ];then
        if [ -z $XAUTHORITY ];then
            export XAUTHORITY=$HOME/.Xauthority
        fi
    fi
fi
EOF
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xhost
%{_mandir}/man1/xhost.1%{_extension}
%{_sysconfdir}/profile.d/*
