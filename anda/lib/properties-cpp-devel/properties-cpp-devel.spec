%global forgeurl https://gitlab.com/ubports/development/core/lib-cpp/properties-cpp
%global commit 7dd9ec00d061d822d259c7477cb12f79d0e1eadd
%forgemeta
%define debug_package %{nil}

Name:           properties-cpp-devel
Version:        0.0.2
Release:        %autorelease
Summary:        A very simple convenience library for handling properties and signals in C++11

License:        LGPL-3.0
URL:            https://gitlab.com/ubports/development/core/lib-cpp/properties-cpp
Source0:        %{url}/-/archive/%commit/properties-cpp-%commit.tar.gz

BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: g++
BuildRequires: gcc
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: doxygen
BuildRequires: cmake-extras

%description
A very simple convenience library for handling properties and signals in C++11.

%package doc
Summary:  properties-cpp documentation files
BuildArch: noarch

%description doc
This package contains documentation files for properties-cpp-devel.

%prep
%autosetup -n properties-cpp-%commit

%build
%cmake

%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_libdir}/pkgconfig/properties-cpp.pc
%{_includedir}/core/*.h

%files doc
%dir %{_docdir}/properties-cpp
%dir %{_docdir}/properties-cpp/html
%{_docdir}/properties-cpp/html/*.html
%{_docdir}/properties-cpp/html/*.map
%{_docdir}/properties-cpp/html/*.css
%{_docdir}/properties-cpp/html/*.png
%{_docdir}/properties-cpp/html/*.js
%{_docdir}/properties-cpp/html/*.md5
%{_docdir}/properties-cpp/html/*.svg

%changelog
%autochangelog
