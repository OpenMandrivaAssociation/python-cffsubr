%global module cffsubr

Name:		python-cffsubr
Version:	0.4.0
Release:	2
Summary:	Standalone CFF subroutinizer based on the AFDKO tx tool
Group:		Development/Python
License:	Apache-2.0
URL:		https://github.com/adobe-type-tools/cffsubr
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	afdko >= 4.0.3
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(fonttools) >= 4.10.2
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	afdko >= 4.0.3

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"

%description
Standalone CFF subroutinizer based on the AFDKO tx tool.

%prep -a
# Remove bundled egg-info
rm -rf src/%{module}.egg-info

# Dont build the extension, it is provided by afdko package.
# Remove custom build backend, as it generates dependencies-
# needed for building the extension.
sed -r -i 's/(ext_modules=)/# \1/' setup.py
sed -r -i 's/^(build-backend|backend-path)/# \1/' pyproject.toml
# Remove the bundled adobe-afdko
rm -rf external

%files
%doc README.md
%license LICENSE
%{_bindir}/%{module}
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}.dist-info
