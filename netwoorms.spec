Summary:	A nibbles clone
Summary(pl):	Klon gry nibbles
Name:		netwoorms
Version:	1.7
Release:	3
Group:		Games
Group(pl):	Gry
Copyright:	Free, but read README
Vendor:		Micha� "Azzie" Marsza�ek <azzie@staszic.waw.pl>
URL:		http://azzie.robotics.net/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
Requires:	zlib
Requires:	ncurses
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetWoorms is a little, multiplayer, networked game, that runs on the
console. If you have ever played 'nibbles', you know the simple rules.
The only difference from the orginal version is that you get frags,
not points, and that you play against as many humans as you want.

%description -l pl
NetWoorms to ma�a gra sieciowa na wielu graczy dzia�aj�ca na konsoli.
Je�li gra�e� kiedy� w 'nibbles', znasz jej proste zasady. Jedyn�
r�nic� mi�dzy NetWoorms a orygina�em jest to, �e gra si� na fragi a
nie punkty i �e mo�na gra� przeciwko dowolnej liczbie ludzi.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make} CFLAGS="$RPM_OPT_FLAGS"

cd contrib/nwoobot-0.3
%configure
%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/netwoorms/{maps,texts}}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install nwoosrv nwoo contrib/nwoobot-0.3/nwoobot $RPM_BUILD_ROOT%{_bindir}
install maps/* $RPM_BUILD_ROOT%{_datadir}/netwoorms/maps
install texts/* $RPM_BUILD_ROOT%{_datadir}/netwoorms/texts
install contrib/maps/* $RPM_BUILD_ROOT%{_datadir}/netwoorms/maps
install contrib/nwoobot-0.3/README README.bot
install docs/* $RPM_BUILD_ROOT%{_mandir}/man1
gzip -9nf LICENSE README NEWS README.bot \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.gz README.gz NEWS.gz README.bot.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/netwoorms
%{_mandir}/man1/*
