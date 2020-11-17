%global service vmware-nsx
%global plugin vmware-nsx-tempest-plugin
%global module vmware_nsx_tempest_plugin
%global with_doc 1

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
It is a tempest plugin to test vmware-nsx at function level. All \
vmware-nsx-tempest-plugin tests are in "master" branch. Some of the tests \
are designed based on N-S traffic. Install this repo on external VM to \
run entire test suite.

Name:       python-%{service}-tests-tempest
Version:    XXX
Release:    XXX
Summary:    Tempest plugin to test Neutron VMware NSX plugin
License:    ASL 2.0
URL:        https://git.openstack.org/cgit/openstack/%{plugin}/

Source0:    http://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz

BuildArch:  noarch
BuildRequires:  git-core
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python3-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python3-%{service}-tests-tempest}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires:   python3-tempest >= 1:18.0.0
Requires:   python3-pbr >= 4.0.0
Requires:   python3-neutron-lib
Requires:   python3-oslo-log >= 3.36.0
Requires:   python3-netaddr
Requires:   python3-six => 1.10.0
Requires:   python3-requests
Requires:   python3-oslo-serialization >= 2.18.0
Requires:   python3-oslo-i18n
Requires:   python3-oslo-config >= 2:5.2.0
Requires:   python3-testtools
Requires:   python3-oslo-utils >= 3.33.0

%description -n python3-%{service}-tests-tempest
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{service}-tests-tempest-doc
Summary:        python-%{service}-tests-tempest documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-%{service}-tests-tempest-doc
It contains the documentation for the %{plugin}.
%endif

%prep
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%{py3_build}

# Generate Docs
%if 0%{?with_doc}
%{__python3} setup.py build_sphinx -b html
# remove the sphinx build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{py3_install}

%files -n python3-%{service}-tests-tempest
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/*.egg-info

%if 0%{?with_doc}
%files -n python-%{service}-tests-tempest-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
