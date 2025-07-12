Summary:	Clone of across/elma games
Summary(pl.UTF-8):	Klon gry across/elma
Name:		xmoto
Version:	0.6.1
Release:	2
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://github.com/xmoto/xmoto/archive/%{version}/%{version}.tar.gz
# Source0-md5:	88725490243e69d5ab5cde349fa5fa3a
Source1:	%{name}.png
Source2:	%{name}.desktop
URL:		http://xmoto.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	gettext-tools
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxdg-basedir-devel >= 1.1.1-2
BuildRequires:	lua51-devel
BuildRequires:	ode-devel >= 1:0.16
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X-Moto is a challenging 2D motocross platform game, where physics play
an all important role in the gameplay. You need to control your bike
to its limit, if you want to have a chance finishing the more
difficult of the challenges.

First you'll try just to complete the levels, while later you'll
compete with yourself and others, racing against the clock.

%description -l pl.UTF-8
X-Moto jest wyzywającą motocrossową dwuwymiarową grą platformową,
gdzie fizyka ma w rozgrywce główną rolę. Panowanie nad motorem musi
być jak najbardziej wyżyłowane, jeżeli chce się myśleć o ukończeniu
trudniejszych poziomów.

Z początku po prostu zalicza się poziomy, później walczy się z
wynikami, swoimi i innych, w wyścigu z czasem.

%prep
%setup -q

# don't run svnversion
touch src/svnVersion

%build
mkdir build
cd build
%cmake .. \
	-DOpenGL_GL_PREFERENCE=GLVND

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

mv -f $RPM_BUILD_ROOT%{_localedir}/ca{_ES,}
mv -f $RPM_BUILD_ROOT%{_localedir}/cs{_CZ,}
mv -f $RPM_BUILD_ROOT%{_localedir}/da{_DK,}
mv -f $RPM_BUILD_ROOT%{_localedir}/gl{_ES,}
mv -f $RPM_BUILD_ROOT%{_localedir}/nb{_NO,}
mv -f $RPM_BUILD_ROOT%{_localedir}/nn{_NO,}
mv -f $RPM_BUILD_ROOT%{_localedir}/sv{_SE,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README.md
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xmoto
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_mandir}/man6/xmoto.*
