%define upstream_name    Parse-ExuberantCTags
%define upstream_version 1.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Efficiently parse exuberant ctags files
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.gz


BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This Perl module parses _ctags_ files and handles both traditional ctags as
well as extended ctags files such as produced with _Exuberant ctags_. To
the best of my knowledge, it does not handle emacs-style "_etags_" files.

The module is implemented as a wrapper around the _readtags_ library that
normally ships with _Exuberant ctags_. If you do not know what that is, you
are encouraged to have a look at the http://ctags.sourceforge.net/ manpage.
In order to use this module, you do not need _Exuberant ctags_ on your
system. The module ships a copy of _readtags_. Quoting the _readtags_
documentation:

  The functions defined in this interface are intended to provide tag file
  support to a software tool. The tag lookups provided are sufficiently fast
  enough to permit opening a sorted tag file, searching for a matching tag,
  then closing the tag file each time a tag is looked up (search times are
  on the order of hundreths of a second, even for huge tag files). This is
  the recommended use of this library for most tool applications. Adhering
  to this approach permits a user to regenerate a tag file at will without
  the tool needing to detect and resynchronize with changes to the tag file.
  Even for an unsorted 24MB tag file, tag searches take about one second.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.20.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 595980
- update to new version 1.02

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-3mdv2011.0
+ Revision: 556069
- rebuild for perl 5.12

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-2mdv2011.0
+ Revision: 552002
- rebuild

* Wed Jul 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.0-1mdv2010.0
+ Revision: 391188
- update to new version 1.01

* Thu Jun 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 388912
- import perl-Parse-ExuberantCTags


* Thu Jun 25 2009 cpan2dist 1.00-1mdv
- initial mdv release, generated with cpan2dist

