#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tenacity
Version  : 6.1.0
Release  : 19
URL      : https://files.pythonhosted.org/packages/de/2c/c705ab21f3638589d75fb529101a9e0b30615f157a639af5b4a87e27ce01/tenacity-6.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/de/2c/c705ab21f3638589d75fb529101a9e0b30615f157a639af5b4a87e27ce01/tenacity-6.1.0.tar.gz
Summary  : Retry code until it succeeds
Group    : Development/Tools
License  : Apache-2.0
Requires: tenacity-license = %{version}-%{release}
Requires: tenacity-python = %{version}-%{release}
Requires: tenacity-python3 = %{version}-%{release}
Requires: monotonic
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : monotonic
BuildRequires : setuptools_scm
BuildRequires : six

%description
Tenacity is a general-purpose retrying library to simplify the task of adding retry behavior to just about anything.

%package license
Summary: license components for the tenacity package.
Group: Default

%description license
license components for the tenacity package.


%package python
Summary: python components for the tenacity package.
Group: Default
Requires: tenacity-python3 = %{version}-%{release}

%description python
python components for the tenacity package.


%package python3
Summary: python3 components for the tenacity package.
Group: Default
Requires: python3-core
Provides: pypi(tenacity)

%description python3
python3 components for the tenacity package.


%prep
%setup -q -n tenacity-6.1.0
cd %{_builddir}/tenacity-6.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582912707
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tenacity
cp %{_builddir}/tenacity-6.1.0/LICENSE %{buildroot}/usr/share/package-licenses/tenacity/1128f8f91104ba9ef98d37eea6523a888dcfa5de
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tenacity/1128f8f91104ba9ef98d37eea6523a888dcfa5de

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
