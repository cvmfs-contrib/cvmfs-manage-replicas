Summary: Manage cvmfs replicas
Name: cvmfs-manage-replicas
Version: 1.0
# The release_prefix macro is used in the OBS prjconf, don't change its name
%define release_prefix 1
Release: %{release_prefix}%{?dist}
BuildArch: noarch
Group: Applications/System
License: BSD
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0: https://github.com/cvmfs-contrib/%{name}/archive/v%{version}.tar.gz

Requires: python-anyjson

%description
Automates the addition and deletion of cvmfs stratum 1 replicas.

%prep
%setup -q

%install
mkdir -p $RPM_BUILD_ROOT/etc/cvmfs
install -p -m 644 manage-replicas.conf $RPM_BUILD_ROOT/etc/cvmfs
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
install -p -m 555 manage-replicas manage-replicas-log $RPM_BUILD_ROOT%{_sbindir}

%files
%config(noreplace) /etc/cvmfs/*
%{_sbindir}/*

%changelog
* Wed Jun 20 2018 Dave Dykstra <dwd@fnal.gov> - 1.0-1
- Initial packaging
