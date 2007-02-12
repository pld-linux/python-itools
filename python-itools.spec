%define		module	itools
%define		pdf_ver 20060321
Summary:	Python package that encapsulates several Python tools
Summary(pl.UTF-8):   Zbiór narzędzi dla Pythona
Name:		python-%{module}
Version:	0.13.2
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.ikaaro.org/download/itools/%{module}-%{version}.tar.gz
# Source0-md5:	3282dd8352ba9085b2fd1f5a8eb5c96e
Source1:	http://www.ikaaro.org/documentation/%{module}-%{pdf_ver}.pdf
# Source1-md5:	5e92187252f907f6ef7464b61e24b8fd
Source2:	http://www.ikaaro.org/download/itools/%{module}-examples.tar.gz
# Source2-md5:	c9a9759752bf7bc606e8fc7b24282f6b
URL:		http://www.ikaaro.org/
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	python-PyXML >= 0.8.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Itools is a Python package that encapsulates several Python tools.

%description -l pl.UTF-8
Itools jest zbiorem narzędzi dla Pythona.

%package doc
Summary:	Documentation for itools modules
Summary(pl.UTF-8):   Dokumentacja do modułów pakietu itools
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%%description doc
This package contains documentation for itools Python modules.

%description doc -l pl.UTF-8
Pakiet zawierający dokumentację dla modułów Pythona z pakietu itools.

%package examples
Summary:	Examples for itools modules
Summary(pl.UTF-8):   Przykłady wykorzystania modułów pakietu itools
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains examples for itools Python modules.

%description examples -l pl.UTF-8
Pakiet zawierający przykładowe programy wykorzystujące moduły Pythona
z pakietu itools.

%prep
%setup -q -n %{module}-%{version}
cp %{SOURCE1} ./
tar -zxf %{SOURCE2}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_examplesdir}/%{name}-%{version},%{_bindir}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" -exec rm -rf {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%{_bindir}/*
%{py_sitescriptdir}/%{module}

%files doc
%defattr(644,root,root,755)
%doc %{module}-%{pdf_ver}.pdf

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
