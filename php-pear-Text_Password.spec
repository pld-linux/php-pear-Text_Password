%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	Password
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - creating passwords with PHP
Summary(pl):	%{_pearname} - tworzenie hase³
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	75d1cb6c91ac2b2afb86385b0dc0d957
URL:		http://pear.php.net/package/Text_Password/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text_Password allows one to create pronounceable and unpronounceable
passwords. The full functional range is explained in the manual at
http://pear.php.net/manual/.

In PEAR status of this package is: %{_status}.

%description -l pl
Za pomoc± Text_Password mo¿liwe jest stworzenie daj±cych siê
wypowiedzieæ (lub nie) hase³. Pe³na funkcjonalno¶æ opisana jest w
podrêczniku dostêpnym pod adresem http://pear.php.net/manual/

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
