%global pypi_name cffsubr

Name:           python-%{pypi_name}
Version:        0.2.9.post1
Release:        1
Summary:        Standalone CFF subroutinizer based on the AFDKO tx tool
Group:          Development/Python
License:        Apache 2.0
URL:            https://github.com/adobe-type-tools/cffsubr
Source0:        http://pypi.python.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(fonttools) >= 4.10.2
BuildRequires:  python3dist(setuptools)
#BuildRequires:  python3dist(setuptools-git-ls-files)
BuildRequires:  python3dist(setuptools-scm)

%{?python_provide:%python_provide python3-%{pypi_name}}
#Requires:       python3dist(afdko)

%description
Standalone CFF subroutinizer based on the AFDKO tx tool.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
export XFLAGS="%{optflags}"
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.md
%{python_sitelib}/%{pypi_name}/
%{python_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
