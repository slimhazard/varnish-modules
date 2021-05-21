# -D MUST pass in _version and _release, and SHOULD pass in dist.

Summary: Varnish VMOD collection
Name: varnish-modules-maxwait
Version: %{_version}
Release: %{_release}%{?dist}
License: BSD
Group: System Environment/Daemons
URL: git@github.com:nigoroll/varnish-modules.git
Source0: %{name}-%{version}.tar.gz

# varnish-maxwait from uplex
Requires: varnish-maxwait = 6.6.0

BuildRequires: varnish-maxwait-devel = 6.6.0
BuildRequires: pkgconfig
BuildRequires: make
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc
BuildRequires: python-sphinx

Provides: varnish-modules-mxwait
Provides: vmod-accept-mxwait, vmod-accept-maxwait
Provides: vmod-bodyaccess-mxwait, vmod-bodyaccess-maxwait
Provides: vmod-header-mxwait, vmod-header-maxwait
Provides: vmod-saintmode-mxwait, vmod-saintmode-maxwait
Provides: vmod-str-mxwait, vmod-str-maxwait
Provides: vmod-tcp-mxwait, vmod-tcp-maxwait
Provides: vmod-var-mxwait, vmod-var-maxwait
Provides: vmod-vsthrottle-mxwait, vmod-vsthrottle-maxwait
Provides: vmod-xkey-mxwait, vmod-xkey-maxwait

%description
Varnish VMOD collection.

Binary compatible with Varnish 6.6 enhanced with the maxwait feature.

%prep
%setup -q -n %{name}-%{version}

%build

%configure

make -j
make rst-docs

%check

make -j check

%install

make install DESTDIR=%{buildroot}

# Only use the version-specific docdir created by %doc below
rm -rf %{buildroot}%{_docdir}

# None of these for fedora/epel
find %{buildroot}/%{_libdir}/ -name '*.la' -exec rm -f {} ';'
find %{buildroot}/%{_libdir}/ -name '*.a' -exec rm -f {} ';'

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/varnish*/vmods/
%{_mandir}/man3/*.3*
%doc README.md COPYING LICENSE CHANGES.rst AUTHORS docs/*.rst

%post
/sbin/ldconfig

%changelog
* Fri May 21 2021 Geoff Simmons <geoff@uplex.de> - %{_version}-%{_release}
- Introduce RPM packaging for el7
- This version is specifically for binary compatibility with
  Varnish 6.6.0 enhanced with the maxwait feature.
