Summary:	Extreme Wave - feature rich, extensible 3D modeling enviroment
Summary(pl):	Extreme Wave - bogate w mo¿liwo¶ci, rozszerzalne ¶rodowisko do modelowania 3D
Name:		ewave
Version:	0.4.0
Release:	0.1
License:	GPL
Group:		Applications/Graphics
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	1278c5e296c5421a6038562d29dee40e
URL:		http://ewave.seul.org/
BuildRequires:	fltk-devel >= 1.0.6
BuildRequires:	guile-devel >= 1.3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extreme Wave is an ambitious project to create a feature rich,
extensible 3D modeling environment.

%description -l pl
Extreme Wave to ambitny projekt stworzenia bogatego w mo¿liwo¶ci,
rozszerzalnego ¶rodowiska do modelowania 3D.

%prep
%setup -q

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__intltoolize}
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
