# Created by pyp2rpm-3.3.4
%global pypi_name cffsubr

Name:           python-%{pypi_name}
Version:        0.2.8
Release:        %mkrel 1
Summary:        Standalone CFF subroutinizer based on the AFDKO tx tool
Group:          Development/Python
License:        Apache 2.0
URL:            https://github.com/adobe-type-tools/cffsubr
Source0:        %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(fonttools) >= 4.10.2
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-git-ls-files)
BuildRequires:  python3dist(setuptools-scm)

%description
Standalone CFF subroutinizer based on the AFDKO tx tool.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3dist(afdko)

%description -n python3-%{pypi_name}
Standalone CFF subroutinizer based on the AFDKO tx tool.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Do not build the extension, which is a copy of the “tx” executable from
# adobe-afdko:
sed -r -i 's/(ext_modules=)/# \1/' setup.py

# Remove bundled adobe-afdko:
rm -rf external

%build
export XFLAGS="%{optflags}"
%py3_build

%install
%py3_install

rm -rf %{buildroot}/%{python3_sitelib}/%{pypi_name}/tx
ln -s %{_bindir}/tx %{buildroot}/%{python3_sitelib}/%{pypi_name}/tx

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
