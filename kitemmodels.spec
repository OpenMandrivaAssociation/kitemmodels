%define major 5
%define libname %mklibname KF5ItemModels %{major}
%define devname %mklibname KF5ItemModels -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kitemmodels
Version:	5.112.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 item model library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickWidgets)
BuildRequires: pkgconfig(Qt5Script)
# For QCH format docs
BuildRequires: qt5-assistant
BuildRequires: doxygen
# No more python bindings in 5.92
Obsoletes: python-%{name} < %{EVRD}

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

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}
%{_datadir}/qlogging-categories5/kitemmodels.categories
%{_datadir}/qlogging-categories5/kitemmodels.renamecategories
%{_libdir}/qt5/qml/org/kde/kitemmodels

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5ItemModels
%{_libdir}/qt5/mkspecs/modules/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
