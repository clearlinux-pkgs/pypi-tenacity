#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tenacity
Version  : 5.0.4
Release  : 7
URL      : https://files.pythonhosted.org/packages/62/27/586b688cf8a9f44c8f3726aa1c8c1f008c01befcc2d3889d55dc95aebaa5/tenacity-5.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/62/27/586b688cf8a9f44c8f3726aa1c8c1f008c01befcc2d3889d55dc95aebaa5/tenacity-5.0.4.tar.gz
Summary  : Retry code until it succeeeds
Group    : Development/Tools
License  : Apache-2.0
Requires: tenacity-license = %{version}-%{release}
Requires: tenacity-python = %{version}-%{release}
Requires: tenacity-python3 = %{version}-%{release}
Requires: futures
Requires: monotonic
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
Tenacity
========
.. image:: https://img.shields.io/pypi/v/tenacity.svg
:target: https://pypi.python.org/pypi/tenacity

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

%description python3
python3 components for the tenacity package.


%prep
%setup -q -n tenacity-5.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554783935
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tenacity
cp LICENSE %{buildroot}/usr/share/package-licenses/tenacity/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tenacity/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
