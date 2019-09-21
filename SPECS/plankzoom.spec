%global common_description %{expand:
Plank is meant to be the simplest dock on the planet. The goal is to
provide just what a dock needs and absolutely nothing more. It is,
however, a library which can be extended to create other dock programs
with more advanced features.

Thus, Plank is the underlying technology for Docky (starting in version
3.0.0) and aims to provide all the core features while Docky extends it
to add fancier things like Docklets, painters, settings dialogs, etc.}

Name:           plankzoom
Summary:        Stupidly simple Dock
Version:        0.11.89
Release:        8%{?dist}
License:        GPLv3+

URL:            https://launchpad.net/%{name}
Source0:        %{url}/1.0/%{version}/+download/plank-%{version}.tar.xz

# patch out support patented MacOS style animation
# Patch0:         00-drop-patented-animation.patch
# Remove patch0 to get zoom icon support

# patch .desktop file to hide the launcher in Pantheon,
# plank is already a default shell component there
# Patch0:         00-hide-in-pantheon.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  vala

BuildRequires:  pkgconfig(cairo) >= 1.13
BuildRequires:  pkgconfig(dbusmenu-glib-0.4) >= 0.4
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(libbamf3) >= 0.2.92
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi) >= 1.6.99.1
BuildRequires:  pkgconfig(xfixes) >= 5.0

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Requires:       bamf-daemon
Requires:       hicolor-icon-theme

%description %{common_description}


%package        libs
Summary:        Shared libraries for %{name}

%description    libs %{common_description}
This package contains the shared libraries.


%package        docklets
Summary:        Docklets for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    docklets %{common_description}
This package contains the docklets for plank.


%package        devel
Summary:        Development files for %{name}

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel %{common_description}
This package contains the files necessary to develop against plank.


%prep
%autosetup -p1


%build
%configure --disable-apport
%make_build


%install
%make_install

%find_lang %{name}

# remove libtool archives from the buildroot
find %{buildroot} -name "*.la" -print -delete

# move appdata file to non-deprecated location
#mv %{buildroot}/%{_datadir}/appdata %{buildroot}/%{_datadir}/metainfo


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{name}.appdata.xml


%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING

%{_bindir}/%{name}

%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/net.launchpad.%{name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/%{name}/

%{_mandir}/man1/%{name}.1*


%files libs
%doc AUTHORS ChangeLog
%license COPYING

%{_libdir}/lib%{name}.so.1*

%dir %{_libdir}/%{name}


%files docklets
%doc AUTHORS ChangeLog
%license COPYING

%dir %{_libdir}/%{name}/docklets
%{_libdir}/%{name}/docklets/*.so


%files devel
%doc AUTHORS ChangeLog
%license COPYING

%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%{_includedir}/%{name}/

%{_datadir}/vala/vapi/%{name}.vapi
%{_datadir}/vala/vapi/%{name}.deps


%changelog
* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.11.4-7
- Hide plank launcher in Pantheon.
- Modernize .spec file.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.4-4
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.4-1
- Update to version 0.11.4.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.3-2
- Make BR on /usr/bin/pkg-config explicit.

* Sun Jan 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.11.3-1
- Update to version 0.11.3.
- Update .spec file for current Packaging Guidelines.

* Fri Aug 19 2016 Wesley Hearn <whearn@redhat.com> - 0.11.2-1
- Updated to latest version

* Fri Mar 25 2016 Wesley Hearn <whearn@redhat.com> - 0.11.0-2
- Fixed issue in the patent patch

* Thu Mar 17 2016 Wesley Hearn <whearn@redhat.com> - 0.11.0-1
- Updated to latest version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 Wesley Hearn <whearn@redhat.com> - 0.10.1-1
- Updated to latest version

* Mon May 04 2015 Wesley Hearn <whearn@redhat.com> - 0.10.0-2
- Disable potential patent issue

* Mon May 04 2015 Wesley Hearn <whearn@redhat.com> - 0.10.0-1
- Updated to latest version

* Mon May 04 2015 Wesley Hearn <whearn@redhat.com> - 0.9.1-1
- Updated to latest upstream

* Wed Jan 28 2015 Wesley Hearn <whearn@redhat.com> - 0.8.1-1
- Updated to latest upstream

* Sat Oct 25 2014 Wesley Hearn <whearn@redhat.com> - 0.7.1-1
- Updated to latest upstream

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Wesley Hearn <whearn@redhat.com> - 0.6.0-1
- New upstream version

* Mon Feb 17 2014 Wesley Hearn <whearn@redhat.com> - 0.5.0-4
- Build against bamf-devel and not bamf4-devel in Fedora 21+

* Mon Feb 17 2014 Wesley Hearn <whearn@redhat.com> - 0.5.0-3
- Removed Group from devel package

* Fri Feb 14 2014 Wesley Hearn <whearn@redhat.com> - 0.5.0-2
- Cleaned up SPEC file

* Tue Jan 14 2014 Wesley Hearn <whearn@redhat.com> - 0.5.0-1
- Updating to new upstream release

* Thu Aug 08 2013 Wesley Hearn <whearn@redhat.com> - 0.3.0-1
- Updating to new upstream release

* Thu Jan 24 2013 Wesley Hearn <whearn@redhat.com> - 0.2.0.734-0.1.20130124bzr
- Updated to 734

* Mon Jan 21 2013 Wesley Hearn <whearn@redhat.com> - 0.2.0.731-1.20130121
- Updates to revision 731
- Fixed version numbers and how I generate the source ball
- Cleaned up spec file some more

* Thu Jan 17 2013 Wesley Hearn <whearn@redhat.com> - 0.0-1.20130117bzr723
- Updated to revision 723
- Cleaned up the spec file some

* Wed Jan 16 2013 Wesley Hearn <whearn@redhat.com> - 0.0-1.20130116bzr722
- Initial package
