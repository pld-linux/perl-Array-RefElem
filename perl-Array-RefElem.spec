#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Array
%define	pnam	RefElem
%include	/usr/lib/rpm/macros.perl
Summary:	Array::RefElem - set up array elements as aliases
Summary(pl.UTF-8):	Array::RefElem - ustawianie elementów tablicy jako aliasów
Name:		perl-Array-RefElem
Version:	1.00
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/G/GA/GAAS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	43ff2dd2049258634cb00697198572d1
URL:		http://search.cpan.org/dist/Array-RefElem/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module gives direct access to some of the internal Perl routines
that let you store things in arrays and hashes.

%description -l pl.UTF-8
Ten moduł daje bezpośredni dostęp do niektórych wewnętrznych funkcji
Perla pozwalających zapisywać różne rzeczy w tablicach i haszach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/Array
%{perl_vendorarch}/Array/*.pm
%dir %{perl_vendorarch}/auto/Array
%dir %{perl_vendorarch}/auto/Array/RefElem
%attr(755,root,root) %{perl_vendorarch}/auto/Array/RefElem/*.so
%{_mandir}/man3/*
