Summary:	Clone of across/elma games
Summary(pl):	Klon gry across/elma
Name:		xmoto
Version:	0.2.0
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/xmoto/%{name}-%{version}-src.tar.gz
# Source0-md5:	0404467792034dd221b92303f2750ac7
Source1:	%{name}.png
Source2:	%{name}.desktop
URL:		http://xmoto.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	libtool
BuildRequires:	lua50-devel
BuildRequires:	ode-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_build_with_as_needed	1

%description
X-Moto is a challenging 2D motocross platform game, where physics play
an all important role in the gameplay. You need to control your bike
to its limit, if you want to have a chance finishing the more
difficult of the challenges.

First you'll try just to complete the levels, while later you'll
compete with yourself and others, racing against the clock.

%description -l pl
X-Moto jest wyzywaj±c± motocrossow± dwuwymiarow± gr± platformow±,
gdzie fizyka ma w rozgrywce g³ówn± rolê. Panowanie nad motorem musi
byæ jak najbardziej wy¿y³owane, je¿eli chce siê my¶leæ o ukoñczeniu
trudniejszych poziomów.

Z pocz±tku po prostu zalicza siê poziomy, pó¼niej walczy siê z
wynikami, swoimi i innych, w wy¶cigu z czasem.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure
%{__make} \
	GL_LIBS="-lGL"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xmoto
%{_pixmapsdir}/*
%{_desktopdir}/*
