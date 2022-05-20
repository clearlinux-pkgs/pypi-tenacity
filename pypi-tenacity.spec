#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-tenacity
Version  : 8.0.1
Release  : 38
URL      : https://files.pythonhosted.org/packages/2c/f5/04748914f5c78f7418b803226bd56cdddd70ac369b936b3e24f5158017f1/tenacity-8.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/2c/f5/04748914f5c78f7418b803226bd56cdddd70ac369b936b3e24f5158017f1/tenacity-8.0.1.tar.gz
Summary  : Retry code until it succeeds
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-tenacity-license = %{version}-%{release}
Requires: pypi-tenacity-python = %{version}-%{release}
Requires: pypi-tenacity-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)

%description
Tenacity
========
.. image:: https://img.shields.io/pypi/v/tenacity.svg
:target: https://pypi.python.org/pypi/tenacity

%package license
Summary: license components for the pypi-tenacity package.
Group: Default

%description license
license components for the pypi-tenacity package.


%package python
Summary: python components for the pypi-tenacity package.
Group: Default
Requires: pypi-tenacity-python3 = %{version}-%{release}

%description python
python components for the pypi-tenacity package.


%package python3
Summary: python3 components for the pypi-tenacity package.
Group: Default
Requires: python3-core
Provides: pypi(tenacity)

%description python3
python3 components for the pypi-tenacity package.


%prep
%setup -q -n tenacity-8.0.1
cd %{_builddir}/tenacity-8.0.1
pushd ..
cp -a tenacity-8.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653058163
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-tenacity
cp %{_builddir}/tenacity-8.0.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-tenacity/1128f8f91104ba9ef98d37eea6523a888dcfa5de
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-tenacity/1128f8f91104ba9ef98d37eea6523a888dcfa5de

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
