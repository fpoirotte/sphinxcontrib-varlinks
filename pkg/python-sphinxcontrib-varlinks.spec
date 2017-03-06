%if 0%{?fedora} || 0%{?rhel} >= 8
%global with_python3 1
%endif

%global srcname sphinxcontrib-varlinks
%global summary Sphinx extension that supports substitutions in hyperlinks
%global common_desc \
This package contains a Sphinx extension that adds support\
for substitutions in hyperlinks, thus making it possible\
to create variable/dynamic links.


Name:       python-%{srcname}
Version:    0.1.1
Release:    1%{?dist}
Summary:    %{summary}

License:    BSD
URL:        https://github.com/fpoirotte/sphinxcontrib-varlinks
Source0:    ../dist/%{srcname}-%{version}.tar.gz
BuildArch:  noarch

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
BuildRequires:  python2-sphinx-testing

%if 0%{?with_python3}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx-testing
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
%setup -q -c

cp -a %{srcname}-%{version} python3-%{srcname}-%{version}


%build
# Python 2 build
pushd %{srcname}-%{version}
%py2_build
popd

%if 0%{?with_python3}
# Python 3 build
pushd python3-%{srcname}-%{version}
%py3_build
popd
%endif


%install
# Python 2 install
pushd %{srcname}-%{version}
%py2_install
popd

%if 0%{?with_python3}
# Python 3 install
pushd python3-%{srcname}-%{version}
%py3_install
popd
%endif


%check
# Test the python 2 build
pushd %{srcname}-%{version}
PYTHONPATH=$PWD nosetests-%{python2_version} -v
popd

%if 0%{?with_python3}
# Test the python 3 build
export LANG=en_US.UTF-8
pushd python3-%{srcname}-%{version}
PYTHONPATH=$PWD nosetests-%{python3_version} -v
popd
%endif


%files -n python2-%{srcname}
%license %{srcname}-%{version}/LICENSE
%{python2_sitelib}/sphinxcontrib/
%{python2_sitelib}/sphinxcontrib_varlinks*

%if 0%{?with_python3}
%files -n python3-%{srcname}
%license python3-%{srcname}-%{version}/LICENSE
%{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/sphinxcontrib_varlinks*
%endif

%changelog
* Mon Mar 06 2017 François Poirotte <clicky@erebot.net> - 0.1.1-1
- Initial packaging

