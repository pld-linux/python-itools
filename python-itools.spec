%include        /usr/lib/rpm/macros.python
%define		module	itools
Summary:	Python package that encapsulates several Python tools
Summary(pl):	Zbiór narzêdzi dla Pythona
Name:		python-%{module}
Version:	0.3.0
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/lleu/%{module}-%{version}.tgz
# Source0-md5:	cd5cc2d1e0b4c29a6d828923d6999756
Patch0:		%{module}-missing_xml.patch
URL:		http://sourceforge.net/projects/lleu/
%pyrequires_eq  python-modules
Requires:	python-PyXML >= 0.8.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Itools is a Python package that encapsulates several Python tools.

%description -l pl
Itools jest zbiorem narzêdzi dla Pythona.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
mkdir docs docs/catalog docs/workflow docs/xml
mv -f {CHANGES.txt,README.txt} docs
mv -f catalog/TODO.txt docs/catalog
mv -f workflow/{HOWTO.txt,TODO.txt} docs/workflow
mv -f xml/{README.txt,TODO.txt} docs/xml
CFLAGS="%{rpmcflags}"
export CLFAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
        --root=$RPM_BUILD_ROOT \
	--optimize=2

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%{py_sitescriptdir}/%{module}
