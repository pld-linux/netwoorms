Summary:	A nibbles clone
Summary(pl):	Klon gry nibbles
Name:		netwoorms
Version:	1.7
Release:	5
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
License:	Free, but read README
Vendor:		Micha³ "Azzie" Marsza³ek <azzie@staszic.waw.pl>
URL:		http://azzie.robotics.net/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetWoorms is a little, multiplayer, networked game, that runs on the
console. If you have ever played 'nibbles', you know the simple rules.
The only difference from the orginal version is that you get frags,
not points, and that you play against as many humans as you want.

%description -l pl
NetWoorms to ma³a gra sieciowa na wielu graczy dzia³aj±ca na konsoli.
Je¶li gra³e¶ kiedy¶ w 'nibbles', znasz jej proste zasady. Jedyn±
ró¿nic± miêdzy NetWoorms a orygina³em jest to, ¿e gra siê na fragi a
nie punkty i ¿e mo¿na graæ przeciwko dowolnej liczbie ludzi.

%prep
%setup -q

%build
./configure --datadir=%{_datadir}
%{__make} CFLAGS="%{rpmcflags}"

cd contrib/nwoobot-0.3
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make} CFLAGS="%{rpmcflags}"

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

gzip -9nf LICENSE README NEWS README.bot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.gz README.gz NEWS.gz README.bot.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/netwoorms
%{_mandir}/man1/*
