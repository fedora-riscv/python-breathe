%global owner michaeljones
%global srcname breathe
%global _description \
Breathe is an extension to reStructuredText and Sphinx to be able to read and \
render the Doxygen xml output.

Name:           python-%{srcname}
Version:        4.34.0
Release:        %autorelease
Summary:        Adds support for Doxygen xml output to reStructuredText and Sphinx

License:        BSD
URL:            https://github.com/%{owner}/%{srcname}
Source0:        %{URL}/archive/v%{version}.tar.gz
Source1:        %{URL}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz.sig
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x8aed58021feacdd5f27ba0e6a72f627716ea9d96#./vermware.key

Patch1:         rhel_sphinx.patch

BuildArch:      noarch

BuildRequires:  doxygen >= 1.8.4
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  %{py3_dist six} >= 1.9
%if 0%{?rhel}
BuildRequires:  %{py3_dist Sphinx}
%else
# Sphinx>=4.0,<6,!=5.0.0
BuildRequires:  ((%{py3_dist Sphinx} >= 4.0 and %{py3_dist Sphinx} < 5.0.0) or (%{py3_dist Sphinx} > 5.0.0 and %{py3_dist Sphinx} < 6))
%endif
BuildRequires:  %{py3_dist docutils} >= 0.12
BuildRequires:  %{py3_dist Jinja2} >= 2.7.3
BuildRequires:  %{py3_dist MarkupSafe} >= 0.23
BuildRequires:  %{py3_dist Pygments} >= 1.6
BuildRequires:  %{py3_dist pytest}
# NOTE: git is only needed because part of the build process checks if it's in
# a git repo
BuildRequires:  git
BuildRequires:  make
BuildRequires:  gnupg2

# Set the name of the documentation directory
%global _docdir_fmt %{name}

%description %_description

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-six
Requires:       doxygen >= 1.8.4
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname} %_description

%package        doc
Summary:        Documentation files for %{srcname}
# tinyxml uses zlib license
License:        BSD and zlib

%description    doc
This package contains documentation for developer documentation for %{srcname}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -n %{srcname}-%{version}
%if 0%{?rhel}
%patch1 -p1
%endif

%build
%py3_build
# Build the documentation
%make_build DOXYGEN=$(which doxygen) PYTHONPATH=$(pwd) html
# Remove temporary build files
rm documentation/build/html/.buildinfo

%install
%py3_install

%check
%make_build dev-test

%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst
%{_bindir}/breathe-apidoc
%{python3_sitelib}/*
%license LICENSE

%files doc
%doc documentation/build/html
%license LICENSE

%changelog
%autochangelog
