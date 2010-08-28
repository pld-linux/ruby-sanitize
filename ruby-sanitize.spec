
%define gitrev d88227e
%define gitauthor rgrove
%define gitproject sanitize

Summary:	Whitelist-based Ruby HTML sanitizer
Name:		ruby-sanitize
Version:	1.2.1
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://download.github.com/%{gitauthor}-%{gitproject}-release-%{version}-0-g%{gitrev}.tar.gz
# Source0-md5:	da84a9359ecaf5eac7a9cea3c2572d99
URL:		http://sanitize.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby
BuildRequires:	ruby-modules
BuildRequires:	setup.rb = 3.4.1
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Whitelist-based Ruby HTML sanitizer.

%prep
%setup -q -n %{gitauthor}-%{gitproject}-%{gitrev}
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--installdirs=std
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/sanitize.rb
%{ruby_rubylibdir}/sanitize
