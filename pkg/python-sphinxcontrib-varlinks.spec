%if 0%{?fedora} || 0%{?rhel} >= 8
%global with_python3 1
%endif

%if "%{_vendor}" == "debian"
%global install_options --install-layout=deb
%endif

%global srcname sphinxcontrib-varlinks
%global summary Sphinx extension that supports substitutions in hyperlinks
%global common_desc \
This package contains a Sphinx extension that adds support\
for substitutions in hyperlinks, thus making it possible\
to create variable/dynamic links.


Name:       python-%{srcname}
Version:    %{pkg_version}
Release:    1%{?dist}
Summary:    %{summary}

License:    BSD
URL:        https://github.com/fpoirotte/sphinxcontrib-varlinks
Source0:    %{curdir}/dist/%{srcname}-%{version}.tar.gz
BuildArch:  noarch

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
BuildRequires:  python2-sphinx-testing
BuildRequires:  python2-nose

%if 0%{?with_python3}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx-testing
BuildRequires: python3-nose
%endif

%description
%common_desc

%package -n    python2-%{srcname}
Summary:       %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%common_desc

%if 0%{?with_python3}
%package -n    python3-%{srcname}
Summary:       %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%common_desc
%endif


%prep
%setup -q -n %{srcname}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'


%build
# Python 2 build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%if 0%{?with_python3}
# Python 3 build
pushd python3-%{srcname}-%{version}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd
%endif


%install
rm -rf %{buildroot}

# Python 2 install
%{__python} setup.py install %{?install_options} --skip-build --root $RPM_BUILD_ROOT

%if 0%{?with_python3}
# Python 3 install
pushd python3-%{srcname}-%{version}
%{__python3} setup.py install %{?install_options} --skip-build --root $RPM_BUILD_ROOT
popd
%endif


%check
# Test the python 2 build
%{__python} setup.py test

%if 0%{?with_python3}
# Test the python 3 build
pushd python3-%{srcname}-%{version}
%{__python3} setup.py test
popd
%endif


%files -n python2-%{srcname}
%doc LICENSE
%{python_sitelib}/sphinxcontrib/
%{python_sitelib}/sphinxcontrib_varlinks*

%if 0%{?with_python3}
%files -n python3-%{srcname}
%doc LICENSE
%{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/sphinxcontrib_varlinks*
%endif

%changelog
* Thu Dec 22 2017 François Poirotte <clicky@erebot.net>
- Improve compatibility with other OSes

* Mon Mar 06 2017 François Poirotte <clicky@erebot.net>
- Initial packaging

