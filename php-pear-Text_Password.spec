%define		_status		stable
%define		_pearname	Text_Password
Summary:	%{_pearname} - creating passwords with PHP
Summary(pl.UTF-8):	%{_pearname} - tworzenie haseł
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	700d47c71eb875403ee26f2c198e8421
URL:		http://pear.php.net/package/Text_Password/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php-pear
Obsoletes:	php-pear-Text_Password-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text_Password allows one to create pronounceable and unpronounceable
passwords. The full functional range is explained in the manual at
http://pear.php.net/manual/.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Za pomocą Text_Password możliwe jest stworzenie dających się
wypowiedzieć (lub nie) haseł. Pełna funkcjonalność opisana jest w
podręczniku dostępnym pod adresem http://pear.php.net/manual/

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Text/*.php
