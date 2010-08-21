%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Services_Yahoo_JP
Summary:	%{_pearname} - WebServices for Yahoo!JAPAN
Summary(pl.UTF-8):	%{_pearname} - WebServices dla Yahoo!JAPAN
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	2
License:	php
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5513e89d489262987a62d5fcade900dd
Patch0:		%{name}-paths.patch
URL:		http://pear.php.net/package/Services_Yahoo_JP/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.3.5
Requires:	php-pear-Services_Yahoo >= 0.0.1
Requires:	php-pear-XML_Parser >= 1.2.7
Requires:	php-pear-XML_Serializer >= 0.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interface for Yahoo!JAPAN Web Services API.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Interfejs dla API Web Services Yahoo!JAPAN.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Services_Yahoo_JP/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/Yahoo/JP
