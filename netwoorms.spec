Summary:	A nibbles clone
Summary(pl.UTF-8):   Klon gry nibbles
Name:		netwoorms
Version:	1.7
Release:	6
License:	Free (see README)
Vendor:		Michał "Azzie" Marszałek <azzie@staszic.waw.pl>
Group:		Applications/Games
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	ddf1ac33c548b5b3112a23bdb6b5ca4c
URL:		http://azzie.home.staszic.waw.pl/?en
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetWoorms is a little, multiplayer, networked game, that runs on the
console. If you have ever played 'nibbles', you know the simple rules.
The only difference from the orginal version is that you get frags,
not points, and that you play against as many humans as you want.

%description -l pl.UTF-8
NetWoorms to mała gra sieciowa na wielu graczy działająca na konsoli.
Jeśli grałeś kiedyś w 'nibbles', znasz jej proste zasady. Jedyną
różnicą między NetWoorms a oryginałem jest to, że gra się na fragi a
nie punkty i że można grać przeciwko dowolnej liczbie ludzi.

%prep
%setup -q

%build
./configure --datadir=%{_datadir}
%{__make} CFLAGS="%{rpmcflags}"

cd contrib/nwoobot-0.3
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/netwoorms/{maps,texts}} \
	$RPM_BUILD_ROOT%{_mandir}/man1

install nwoosrv nwoo contrib/nwoobot-0.3/nwoobot $RPM_BUILD_ROOT%{_bindir}
install maps/* $RPM_BUILD_ROOT%{_datadir}/netwoorms/maps
install texts/* $RPM_BUILD_ROOT%{_datadir}/netwoorms/texts
install contrib/maps/* $RPM_BUILD_ROOT%{_datadir}/netwoorms/maps
install contrib/nwoobot-0.3/README README.bot
install docs/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README NEWS README.bot
%attr(755,root,root) %{_bindir}/*
%{_datadir}/netwoorms
%{_mandir}/man1/*
