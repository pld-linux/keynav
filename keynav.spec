#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	Keyboard pointer navigation
Name:		keynav
Version:	0.20100601.2912
Release:	0.1
License:	MIT
Group:		Applications
Source0:	http://semicomplete.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	2b1113d2337d7bef5742a7f3ab04cf23
URL:		http://www.semicomplete.com/projects/keynav/
BuildRequires:	pkgconfig
BuildRequires:	xdotool-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
keynav is a piece of an on-going experiment to make pointer-driven
interfaces easier and faster for users to operate. It lets you move
the pointer quickly to most points on the screen with only a few key
strokes.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags} $(pkg-config --libs xext)" \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir} $RPM_BUILD_ROOT%{_bindir}
cp keynavrc $RPM_BUILD_ROOT%{_sysconfdir}/keynavrc
cp keynav $RPM_BUILD_ROOT%{_bindir}/keynav

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELIST README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/keynavrc
%attr(755,root,root) %{_bindir}/keynav
