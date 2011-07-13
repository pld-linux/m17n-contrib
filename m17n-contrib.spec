Summary:	Contributed database for the multilingual text processing library
#Summary(pl.UTF-8):	-
Name:		m17n-contrib
Version:	1.1.12
Release:	1
License:	LGPL
Group:		Applications
Source0:	http://www.m17n.org/m17n-lib-download/%{name}-%{version}.tar.gz
# Source0-md5:	fb7c35194e8940cf3ca381f5b111434c
URL:		http://www.m17n.org/
BuildRequires:	m17n-db
Requires:	m17n-db
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the database files contributed by the community
and used by m17n-lib.

#%description -l pl.UTF-8

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang m17n-contrib

%clean
rm -rf $RPM_BUILD_ROOT

%files -f m17n-contrib.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/m17n/icons/*
%{_datadir}/m17n/*.mim
%{_datadir}/m17n/scripts
