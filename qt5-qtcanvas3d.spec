%global qt_module qtcanvas3d

%define docs 1

Summary: Qt5 - Canvas3d component
Name:    qt5-%{qt_module}
Version: 5.9.7
Release: 1%{?dist}

License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://www.qt.io
Source0: http://download.qt.io/official_releases/qt/5.9/%{version}/submodules/%{qt_module}-opensource-src-%{version}.tar.xz

BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-static
BuildRequires: qt5-qtdeclarative-devel

%{?_qt5_version:Requires: qt5-qtbase%{?_isa} >= %{_qt5_version}}

%description
Qt5 Canvas3D component

%if 0%{?docs}
%package doc
Summary: API documentation for %{name}
License: GFDL
Requires: %{name} = %{version}-%{release}
BuildRequires: qt5-qdoc
BuildRequires: qt5-qhelpgenerator
BuildArch: noarch
%description doc
%{summary}.
%endif

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%setup -q -n %{qt_module}-opensource-src-%{version}


%build
%{qmake_qt5}

make %{?_smp_mflags}


%if 0%{?docs}
# HACK to avoid multilib conflicts in noarch content
# see also https://bugreports.qt-project.org/browse/QTBUG-42071
QT_HASH_SEED=0; export QT_HASH_SEED
make %{?_smp_mflags} docs
%endif


%install
make install INSTALL_ROOT=%{buildroot}

%if 0%{?docs}
make install_docs INSTALL_ROOT=%{buildroot}
%endif


%files
%license LICENSE.*
%{_qt5_archdatadir}/qml/QtCanvas3D/

%if 0%{?docs}
%files doc
%{_qt5_docdir}/%{qt_module}.qch
%{_qt5_docdir}/%{qt_module}/
%endif

%files examples
%{_qt5_examplesdir}/canvas3d/


%changelog
* Thu Feb 07 2019 Jan Grulich <jgrulich@redhat.com> - 5.9.7-1
- Update to 5.9.7
  Resolves: bz#1564001

* Fri Oct 06 2017 Jan Grulich <jgrulich@redhat.com> - 5.9.2-1
- Update to 5.9.2
  Resolves: bz#1482775

* Wed Aug 23 2017 Jan Grulich <jgrulich@redhat.com> - 5.9.1-1
- Update to 5.9.1
  Resolves: bz#1482775

* Wed Jan 11 2017 Jan Grulich <jgrulich@redhat.com> - 5.6.2-1
- Update to 5.6.2
  Resolves: bz#1384815

* Tue Aug 30 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.1-10
- Increase build version to have newer version than in EPEL
  Resolves: bz#1317398

* Wed Jun 08 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.1-1
- Update to 5.6.1
  Resolves: bz#1317398

* Wed Apr 13 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.0-5
- Enable documentation
  Resolves: bz#1317398

* Thu Apr 07 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.0-4
- Initial version for RHEL
  Resolves: bz#1317398

* Sun Mar 20 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.0-3
- rebuild

* Fri Mar 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.0-2
- rebuild

* Mon Mar 14 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-1
- 5.6.0 final release

* Tue Feb 23 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.6.rc
- Update to final RC

* Mon Feb 15 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.5
- Update RC release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-0.4.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Rex Dieter <rdieter@fedoraproject.org> 5.6.0-0.3.beta
- respin sources, use %%license, update URLs, fix -doc BR's, drop unneeded scriptlets

* Thu Dec 10 2015 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.2
- Official beta release

* Tue Nov 03 2015 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.1
- Start to implement 5.6.0 beta

* Tue Nov 03 2015 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.1
- Start to implement 5.6.0 beta

* Thu Oct 15 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.1-2
- Update to final release 5.5.1

* Tue Sep 29 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.1-1
- Update to Qt 5.5.1 RC1

* Wed Jul 1 2015 Helio Chissini de Castro <helio@kde.org> 5.5.0-1
- New final upstream release Qt 5.5.0

* Thu Jun 25 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.0-0.2.rc
- Update for official RC1 released packages

* Thu Jun 25 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.0-0.1.rc
- Initial release
