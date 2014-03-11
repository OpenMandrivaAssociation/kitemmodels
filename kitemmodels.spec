%define major 5
%define libname %mklibname KF5ItemModels %{major}
%define devname %mklibname KF5ItemModels -d
%define debug_package %{nil}

Name: kitemmodels
Version: 4.97.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 item model library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5

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
%cmake

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5ItemModels
%{_libdir}/qt5/mkspecs/modules/*
