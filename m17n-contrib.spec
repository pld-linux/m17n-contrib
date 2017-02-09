Summary:	Contributed database for the multilingual text processing library
Summary(pl.UTF-8):	Społecznościowa baza danych do biblioteki przetwarzania tekstu wielojęzycznego
Name:		m17n-contrib
Version:	1.1.14
Release:	1
License:	LGPL v2.1+
Group:		Applications/Text
Source0:	http://download.savannah.gnu.org/releases/m17n/%{name}-%{version}.tar.gz
# Source0-md5:	ae8c8b57604144a3d40afe54d5a912a3
URL:		http://www.m17n.org/
BuildRequires:	m17n-db
Requires:	m17n-db
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the database files contributed by the community
and used by m17n-lib.

%description -l pl.UTF-8
Ten pakiet zawiera pliki baz danych udostępnione przez społeczność do
wykorzystania przez m17n-lib.

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
%{_datadir}/m17n/icons/*.png
%{_datadir}/m17n/*.mim
%{_datadir}/m17n/scripts
