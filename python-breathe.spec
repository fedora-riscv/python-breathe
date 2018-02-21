%global owner michaeljones
%global srcname breathe
%global _description \
Breathe is an extension to reStructuredText and Sphinx to be able to read and \
render the Doxygen xml output.

Name:           python-%{srcname}
Version:        4.7.3
Release:        3%{?dist}
Summary:        Adds support for Doxygen xml output to reStructuredText and Sphinx

License:        BSD
URL:            https://github.com/%{owner}/%{srcname}
Source0:        https://github.com/%{owner}/%{srcname}/archive/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  doxygen
BuildRequires:  python2-devel python%{python3_pkgversion}-devel
BuildRequires:  python2-setuptools python%{python3_pkgversion}-setuptools
BuildRequires:  python2-six python%{python3_pkgversion}-six
BuildRequires:  python2-sphinx
# NOTE: git is only needed because part of the build process checks if it's in
# a git repo
BuildRequires:  git

# Set the name of the documentation directory
%global _docdir_fmt %{name}

%description %_description

%package -n     python2-%{srcname}
Summary:        %{summary}
Requires:       python2-six
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
%autosetup -n %{srcname}-%{version}

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
* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.7.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 24 2017 Dave Johansen <davejohansen@gmail.com> - 4.7.3-1
- Upstream update

* Tue Aug 22 2017 Dave Johansen <davejohansen@gmail.com> - 4.7.2-1
- Upstream update

* Wed Aug 16 2017 Dave Johansen <davejohansen@gmail.com> - 4.7.1-1
- Upstream update

* Wed Aug 09 2017 Dave Johansen <davejohansen@gmail.com> - 4.7.0-1
- Upstream update

* Sat Aug 05 2017 Dave Johansen <davejohansen@gmail.com> - 4.6.0-3
- Fix for node without parent

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Miro Hrončok <mhroncok@redhat.com> - 4.6.0-1
- Upstream update

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Miro Hrončok <mhroncok@redhat.com> - 4.4.0-2
- Rebuild for Python 3.6

* Mon Dec 19 2016 Dave Johansen <davejohansen@gmail.com> - 4.4.0-1
- Upstream release

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
