%define major 5
%define libname %mklibname KF5ItemModels %{major}
%define devname %mklibname KF5ItemModels -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kitemmodels
Version:	5.17.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 item model library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)

%description
The ItemModels framework contains data models on top of
QAbstractItemModel that help in common tasks, such as sorting, proxying
and filtering.

ItemModels contains useful classes such as a model for checkable or
selectable items, recursive filtering and breadcrumb selection.

%package -n %{libname}
Summary: The KDE Frameworks 5 item model library
Group: System/Libraries

%description -n %{libname}
The ItemModels framework contains data models on top of
QAbstractItemModel that help in common tasks, such as sorting, proxying
and filtering.

ItemModels contains useful classes such as a model for checkable or
selectable items, recursive filtering and breadcrumb selection.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

The ItemModels framework contains data models on top of
QAbstractItemModel that help in common tasks, such as sorting, proxying
and filtering.

ItemModels contains useful classes such as a model for checkable or
selectable items, recursive filtering and breadcrumb selection.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5ItemModels
%{_libdir}/qt5/mkspecs/modules/*
