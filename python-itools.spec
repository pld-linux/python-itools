%define		module	itools
Summary:	Python package that encapsulates several Python tools
Summary(pl):	Zbiór narzêdzi dla Pythona
Name:		python-%{module}
Version:	0.6.2
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.ikaaro.org/download/itools/%{module}-%{version}.tar.gz
# Source0-md5:	e0aadd6779aa08231dddf37d4a529450
Source1:	http://www.ikaaro.org/download/itools/%{module}-%{version}.pdf
# Source1-md5:	8eb29b3828c3df853021545077fe0429
URL:		http://www.ikaaro.org/
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	python-PyXML >= 0.8.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Itools is a Python package that encapsulates several Python tools.

%description -l pl
Itools jest zbiorem narzêdzi dla Pythona.

%package doc
Summary:	Documentation for itools modules
Summary(pl):	Dokumentacja do modu³ów pakietu itools
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%%description doc
This package contains documentation for itools Python modules.

%description doc -l pl
Pakiet zawieraj±cy dokumentacjê dla modu³ów Pythona z pakietu itools.

%package examples
Summary:	Examples for itools modules
Summary(pl):	Przyk³ady wykorzystania modu³ów pakietu itools
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains examples for itools Python modules.

%description examples -l pl
Pakiet zawieraj±cy przyk³adowe programy wykorzystuj±ce modu³y Pythona
z pakietu itools.

%prep
%setup -q -n %{module}-%{version}
cp %{SOURCE1} doc

%build
mkdir docs docs/workflow docs/xml
mv -f {CHANGES.txt,README.txt} docs
mv -f workflow/{HOWTO.txt,TODO.txt} docs/workflow
mv -f xml/TODO.txt docs/xml
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_examplesdir}/%{name}-%{version},%{_bindir}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

cp -a doc/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" -exec rm -rf {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%{_bindir}/igettext.py
%{py_sitescriptdir}/%{module}

%files doc
%defattr(644,root,root,755)
%doc doc/%{module}-%{version}.pdf

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
