Summary:	DVD navigation plugin for Xine
Summary(pl):	Plugin DVD dla Xine
Name:		xine-dvdnav
Version:	0.9.8.beta2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://prdownloads.sourceforge.net/dvd/%{name}-%{version}.tar.gz
URL:		http://dvd.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdvdread-devel
BuildRequires:	libtool
BuildRequires:	xine-lib-devel >= 0.9.3
Requires:	xine-ui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_pluginsdir	%{_libdir}/xine/plugins

%description
This is DVD-navigation plugin for xine.

If you also have libdvdcss installed it will make xine play
CSS-encrypted DVDs.

%description -l pl
Plugin nawigacji DVD dla xine.

Gdy jest zainstalowany tak�e pakiet libdvdcss modu� ten mo�e s�u�y� do
odtwarzania kodowany p�yt DVD.

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=$RPM_BUILD_ROOT%{_datadir}/doc/xine

gzip -9nf *README* AUTHORS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_pluginsdir}/*
