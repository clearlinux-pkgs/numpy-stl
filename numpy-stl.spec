#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE81444E9CE1F695D (wolph@wol.ph)
#
Name     : numpy-stl
Version  : 2.16.0
Release  : 25
URL      : https://github.com/WoLpH/numpy-stl/releases/download/v2.16.0/numpy-stl-v2.16.0.tar.xz
Source0  : https://github.com/WoLpH/numpy-stl/releases/download/v2.16.0/numpy-stl-v2.16.0.tar.xz
Source1  : https://github.com/WoLpH/numpy-stl/releases/download/v2.16.0/numpy-stl-v2.16.0.tar.xz.asc
Summary  : Library to make reading, writing and modifying both binary and ascii STL files easy.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: numpy-stl-bin = %{version}-%{release}
Requires: numpy-stl-license = %{version}-%{release}
Requires: numpy-stl-python = %{version}-%{release}
Requires: numpy-stl-python3 = %{version}-%{release}
Requires: numpy
Requires: python-utils
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : numpy
BuildRequires : python-utils

%description
numpy-stl
==============================================================================

%package bin
Summary: bin components for the numpy-stl package.
Group: Binaries
Requires: numpy-stl-license = %{version}-%{release}

%description bin
bin components for the numpy-stl package.


%package license
Summary: license components for the numpy-stl package.
Group: Default

%description license
license components for the numpy-stl package.


%package python
Summary: python components for the numpy-stl package.
Group: Default
Requires: numpy-stl-python3 = %{version}-%{release}

%description python
python components for the numpy-stl package.


%package python3
Summary: python3 components for the numpy-stl package.
Group: Default
Requires: python3-core
Provides: pypi(numpy_stl)
Requires: pypi(numpy)
Requires: pypi(python_utils)

%description python3
python3 components for the numpy-stl package.


%prep
%setup -q -n numpy-stl-v2.16.0
cd %{_builddir}/numpy-stl-v2.16.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617033646
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/numpy-stl
cp %{_builddir}/numpy-stl-v2.16.0/LICENSE %{buildroot}/usr/share/package-licenses/numpy-stl/7f2ba3d85548b142cdd896317a0a190793940c1f
cp %{_builddir}/numpy-stl-v2.16.0/docs/_theme/LICENSE %{buildroot}/usr/share/package-licenses/numpy-stl/3d1c6f6ce9ac9fdbae7bdc2b4d63940561f79edd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/stl
/usr/bin/stl2ascii
/usr/bin/stl2bin

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/numpy-stl/3d1c6f6ce9ac9fdbae7bdc2b4d63940561f79edd
/usr/share/package-licenses/numpy-stl/7f2ba3d85548b142cdd896317a0a190793940c1f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
