Summary:	DVD navigation plugin for Xine
Summary(pl):	Wtyczka DVD dla Xine
Name:		xine-dvdnav
Version:	0.9.13
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/dvd/%{name}-%{version}.tar.gz
URL:		http://dvd.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdvdread-devel
BuildRequires:	libtool
BuildRequires:	xine-lib-devel >= 0.9.13
BuildRequires:	libdvdnav-devel >= 0.1.0
%requires_eq	xine-lib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_pluginsdir	%{_libdir}/xine/plugins

%description
This is DVD-navigation plugin for xine.

If you also have libdvdcss installed it will make xine play
CSS-encrypted DVDs.

%description -l pl
Wtyczka nawigacji DVD dla xine.

Gdy jest zainstalowany tak¿e pakiet libdvdcss, modu³ ten mo¿e s³u¿yæ
do odtwarzania kodowanych p³yt DVD.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=$RPM_BUILD_ROOT%{_datadir}/doc/xine

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *README* AUTHORS ChangeLog
%attr(755,root,root) %{_pluginsdir}/*
