Name:		texlive-siunitx
Version:	2.7s
Release:	1
Summary:	A comprehensive (SI) units package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/siunitx
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/siunitx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/siunitx.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/siunitx.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Typesetting values with units requires care to ensure that the
combined mathematical meaning of the value plus unit
combination is clear. In particular, the SI units system lays
down a consistent set of units with rules on how they are to be
used. However, different countries and publishers have
differing conventions on the exact appearance of numbers (and
units). A number of LaTeX packages have been developed to
provide consistent application of the various rules: SIunits,
sistyle, unitsdef and units are the leading examples. The
numprint package provides a large number of number-related
functions, while dcolumn and rccol provide tools for
typesetting tabular numbers. The siunitx package takes the best
from the existing packages, and adds new features and a
consistent interface. A number of new ideas have been
incorporated, to fill gaps in the existing provision. The
package also provides backward-compatibility with SIunits,
sistyle, unitsdef and units. The aim is to have one package to
handle all of the possible unit-related needs of LaTeX users.
The package relies on LaTeX 3 support from the l3kernel and
l3packages bundles.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/siunitx
%doc %{_texmfdistdir}/doc/latex/siunitx
#- source
%doc %{_texmfdistdir}/source/latex/siunitx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
