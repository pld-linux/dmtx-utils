Summary:	Utilities for libdmtx
Name:		dmtx-utils
Version:	0.7.4
Release:	8
License:	LGPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/libdmtx/%{name}-%{version}.tar.bz2
# Source0-md5:	b132ab9fb1d289869469b8bb4959a08a
Patch0:		ac.patch
Patch1:		imagemagick7.patch
URL:		http://www.libdmtx.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libdmtx-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.219
Obsoletes:	libdmtx-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains utilities that use libdmtx.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING.LESSER ChangeLog KNOWNBUG NEWS README README.linux TODO
%attr(755,root,root) %{_bindir}/dmtxquery
%attr(755,root,root) %{_bindir}/dmtxread
%attr(755,root,root) %{_bindir}/dmtxwrite
%{_mandir}/man1/dmtxquery.1*
%{_mandir}/man1/dmtxread.1*
%{_mandir}/man1/dmtxwrite.1*
