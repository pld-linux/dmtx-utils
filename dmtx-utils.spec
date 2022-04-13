Summary:	Utilities for libdmtx
Summary(pl.UTF-8):	Narzędzia do libdmtx
Name:		dmtx-utils
Version:	0.7.6
Release:	1
License:	LGPL v2+
Group:		Applications/System
#Source0Download: https://github.com/dmtx/dmtx-utils/tags
Source0:	https://github.com/dmtx/dmtx-utils/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c7777dc5db7d7c723e890075a4a5227e
Patch0:		ac.patch
URL:		http://libdmtx.sourceforge.net/
BuildRequires:	ImageMagick-devel >= 1:6.2.4
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libdmtx-devel >= 0.7.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	ImageMagick-libs >= 1:6.2.4
Requires:	libdmtx >= 0.7.0
Obsoletes:	libdmtx-utils < 0.7.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains utilities that use libdmtx.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia wykorzystujące libdmtx

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
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
%doc AUTHORS ChangeLog KNOWNBUG README README.linux TODO
%attr(755,root,root) %{_bindir}/dmtxquery
%attr(755,root,root) %{_bindir}/dmtxread
%attr(755,root,root) %{_bindir}/dmtxwrite
%{_mandir}/man1/dmtxquery.1*
%{_mandir}/man1/dmtxread.1*
%{_mandir}/man1/dmtxwrite.1*
