Name: xhost
Version: 1.0.6
Release: 8
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
%configure2_5x
%make

%install
%makeinstall_std


%files
%{_bindir}/xhost
%{_mandir}/man1/xhost.1%{_extension}


%changelog
* Mon Mar 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.5-1
+ Revision: 786805
- version update 1.0.5

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2
+ Revision: 671321
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 591824
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.3-1mdv2010.1
+ Revision: 464708
- New version: 1.0.3

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.2-8mdv2009.1
+ Revision: 351078
- rebuild

* Mon Aug 04 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1.0.2-7mdv2009.0
+ Revision: 263480
- Drop xhost.sh. It sets XAUTHORITY to the same value used when it is not set.

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-6mdv2009.0
+ Revision: 226044
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-5mdv2008.1
+ Revision: 154732
- Updated BuildRequires and resubmit package.

* Tue Jan 15 2008 Christiaan Welvaart <spturtle@mandriva.org> 1.0.2-4mdv2008.1
+ Revision: 153294
- protect the $ (in xhost profile scriptlets)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-3mdv2008.1
+ Revision: 119060
- ship xhost profile scriptlet

* Tue Jul 17 2007 Colin Guthrie <cguthrie@mandriva.org> 1.0.2-1mdv2008.0
+ Revision: 52838
- New upstream release 1.0.2

