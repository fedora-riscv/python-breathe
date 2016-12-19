%global owner michaeljones
%global commit0 a423389dfe2935962b3b27586602cfc3521fb54a
%global srcname breathe
%global _description \
Breathe is an extension to reStructuredText and Sphinx to be able to read and \
render the Doxygen xml output.

Name:           python-%{srcname}
Version:        4.2.0
Release:        5%{?dist}
Summary:        Adds support for Doxygen xml output to reStructuredText and Sphinx

License:        BSD
URL:            https://github.com/%{owner}/%{srcname}
Source0:        https://github.com/%{owner}/%{srcname}/archive/%{commit0}.tar.gz#/%{srcname}-%{commit0}.tar.gz
Patch0:         breathe_python3.patch

BuildArch:      noarch

BuildRequires:  doxygen
BuildRequires:  python2-devel python%{python3_pkgversion}-devel
BuildRequires:  python-setuptools python%{python3_pkgversion}-setuptools
BuildRequires:  python-six python%{python3_pkgversion}-six
BuildRequires:  python-sphinx
# NOTE: git is only needed because part of the build process checks if it's in
# a git repo
BuildRequires:  git

# Set the name of the documentation directory
%global _docdir_fmt %{name}

%description %_description

%package -n     python2-%{srcname}
Summary:        %{summary}
Requires:       python-six
%{?python_provide:%python_provide python2-%{srcname}}

# This package replaces the old version packaged as just breathe
Provides:       %{srcname} = %{version}-%{release}
Obsoletes:      %{srcname} < %{version}-%{release}

%description -n python2-%{srcname} %_description

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-six
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname} %_description

%package        doc
Summary:        Documentation files for %{srcname}
# tinyxml uses zlib license
License:        BSD and zlib

%description    doc
This package contains documentation for developer documentation for %{srcname}.

%prep
%autosetup -n %{srcname}-%{commit0} -p1

%build
%py2_build
%py3_build
# Build the documentation
make %{?_smp_mflags} html
# Remove temporary build files
rm documentation/build/html/.buildinfo

%install
%py2_install
%py3_install

%files -n python2-%{srcname}
%{python2_sitelib}/*
%license LICENSE

%files -n python%{python3_pkgversion}-%{srcname}
%{_bindir}/breathe-apidoc
%{python3_sitelib}/*
%license LICENSE

%files doc
%doc documentation/build/html
%license LICENSE

%changelog
* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.2.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 13 2016 Dave Johansen <davejohansen@gmail.com> - 4.2.0-3
- Fix for Python 3

* Sun Apr 10 2016 Orion Poplawski <orion@cora.nwra.com> - 4.2.0-2
- Fix BR/Rs

* Wed Apr 06 2016 Dave Johansen <davejohansen@gmail.com> - 4.2.0-1
- Initial RPM release
