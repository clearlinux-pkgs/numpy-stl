#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE81444E9CE1F695D (wolph@wol.ph)
#
Name     : numpy-stl
Version  : 2.10.1
Release  : 8
URL      : https://github.com/WoLpH/numpy-stl/releases/download/v2.10.1/numpy-stl-v2.10.1.tar.xz
Source0  : https://github.com/WoLpH/numpy-stl/releases/download/v2.10.1/numpy-stl-v2.10.1.tar.xz
Source99 : https://github.com/WoLpH/numpy-stl/releases/download/v2.10.1/numpy-stl-v2.10.1.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: numpy-stl-bin = %{version}-%{release}
Requires: numpy-stl-license = %{version}-%{release}
Requires: numpy-stl-python = %{version}-%{release}
Requires: numpy-stl-python3 = %{version}-%{release}
Requires: numpy
Requires: python-utils
BuildRequires : buildreq-distutils3
BuildRequires : numpy
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytest-runner
BuildRequires : python-utils
BuildRequires : tox
BuildRequires : virtualenv

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

%description python3
python3 components for the numpy-stl package.


%prep
%setup -q -n numpy-stl-v2.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555172073
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/numpy-stl
cp LICENSE %{buildroot}/usr/share/package-licenses/numpy-stl/LICENSE
cp docs/_theme/LICENSE %{buildroot}/usr/share/package-licenses/numpy-stl/docs__theme_LICENSE
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
/usr/share/package-licenses/numpy-stl/LICENSE
/usr/share/package-licenses/numpy-stl/docs__theme_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
