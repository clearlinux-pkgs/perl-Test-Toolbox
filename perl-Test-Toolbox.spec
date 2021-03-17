#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Toolbox
Version  : 0.4
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIKO/Test-Toolbox-0.4.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIKO/Test-Toolbox-0.4.tar.gz
Summary  : 'Test::Toolbox - tools for testing'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Toolbox-license = %{version}-%{release}
Requires: perl-Test-Toolbox-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Test::Toolbox - tools for testing
SYNOPSIS
# load module
use Test::Toolbox;

# plan tests
rtplan 43;

# or, plan tests, but die on the first failure
rtplan 43, autodie=>1;

# basic test
rtok 'my test name', $success;

# test for failure if you prefer
rtok 'test name', $success, should=>0;

# two values should equal each other
rtcomp 'test name', $val, $other_val;

# two values should not equal each other
rtcomp 'test name', $val, $other_val, should=>0;

# run some code which should succeed
# note that the second param is undef
rteval 'test name', undef, sub { mysub() };

# run some code which should cause a specific error code
rteval 'test name', 'file-open-failed', sub { mysub() };

# check that $@ has a specific error code
rtid 'test name', $@, 'missing-keys';

# much more

%package dev
Summary: dev components for the perl-Test-Toolbox package.
Group: Development
Provides: perl-Test-Toolbox-devel = %{version}-%{release}
Requires: perl-Test-Toolbox = %{version}-%{release}

%description dev
dev components for the perl-Test-Toolbox package.


%package license
Summary: license components for the perl-Test-Toolbox package.
Group: Default

%description license
license components for the perl-Test-Toolbox package.


%package perl
Summary: perl components for the perl-Test-Toolbox package.
Group: Default
Requires: perl-Test-Toolbox = %{version}-%{release}

%description perl
perl components for the perl-Test-Toolbox package.


%prep
%setup -q -n Test-Toolbox-0.4
cd %{_builddir}/Test-Toolbox-0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Toolbox
cp %{_builddir}/Test-Toolbox-0.4/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Toolbox/a1f666cec80d835a358658aaaf60d4a864dc068c
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Toolbox.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Toolbox/a1f666cec80d835a358658aaaf60d4a864dc068c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Test/Toolbox.pm
/usr/lib/perl5/vendor_perl/5.32.1/Test/Toolbox.pod
