Summary:	Clone of across/elma games
Summary(pl.UTF-8):	Klon gry across/elma
Name:		xmoto
Version:	0.3.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.tuxfamily.org/xmoto/xmoto/%{version}/%{name}-%{version}-src.tar.gz
# Source0-md5:	f1f7726a8856f9c9efa2ae8e3192bb7f
Source1:	%{name}.png
Source2:	%{name}.desktop
Source3:	%{name}.6
Patch0:		%{name}-libs.patch
URL:		http://xmoto.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	lua50-devel
BuildRequires:	ode-devel
BuildRequires:	pkgconfig
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
cat %{SOURCE3} | gzip -9 > xmoto.6.gz
#%patch0 -p1

# fix lv translation
sed -i -e 's/lv_LV/lv/g' configure.in
mv -f po/lv{_LV,}.po

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I config
%{__autoconf}
%{__automake}

%configure \
	--with-enable-zoom=1
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

mv -f $RPM_BUILD_ROOT%{_mandir}/{mang,man6}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/ca{_ES,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/cs{_CZ,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/de{_DE,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/es{_ES,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/fi{_FI,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/fr{_FR,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/it{_IT,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/nb{_NO,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/nn{_NO,}
rm -fr $RPM_BUILD_ROOT%{_datadir}/locale/no*
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/pl{_PL,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/ru{_RU,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sk{_SK,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sv{_SE,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xmoto
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_mandir}/man6/*
