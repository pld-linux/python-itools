%define		module	itools
Summary:	Python package that encapsulates several Python tools
Summary(pl):	Zbiór narzêdzi dla Pythona
Name:		python-%{module}
Version:	0.5.0
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/lleu/%{module}-%{version}.tar.gz
# Source0-md5:	8b8e87d4b9b6f51f0a899be7803ee2f6
URL:		http://sourceforge.net/projects/lleu/
%pyrequires_eq	python-modules
Requires:	python-PyXML >= 0.8.2
#BuildRequires:	tetex-dvips
#BuildRequires:	tetex-latex
#BuildRequires:	tetex-format-latex
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	python-itools-doc

%description
Itools is a Python package that encapsulates several Python tools.

%description -l pl
Itools jest zbiorem narzêdzi dla Pythona.

#%%package doc
#Summary:	Documentation for itools modules
#Summary(pl):	Dokumentacja do modu³ów pakietu itools
#Group:		Libraries/Python
#Requires:	%{name} = %{version}-%{release}

#%%description doc
#This package contains documentation for itools Python modules.

#%%description doc -l pl
#Pakiet zawieraj±cy dokumentacjê dla modu³ów Pythona z pakietu itools.

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

# %{__make} -C doc ps

cp -a doc/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" -exec rm -rf {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%{_bindir}/igettext.py
%{py_sitescriptdir}/%{module}

#%%files doc
#%%defattr(644,root,root,755)
#%%doc doc/itools.ps

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
