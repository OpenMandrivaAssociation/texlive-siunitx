# revision 27181
# category Package
# catalog-ctan /macros/latex/contrib/siunitx
# catalog-date 2012-07-22 18:49:09 +0200
# catalog-license lppl1.3
# catalog-version 2.5g
Name:		texlive-siunitx
Version:	2.5g
Release:	2
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
%{_texmfdistdir}/tex/latex/siunitx/config/siunitx-abbreviations.cfg
%{_texmfdistdir}/tex/latex/siunitx/config/siunitx-binary.cfg
%{_texmfdistdir}/tex/latex/siunitx/config/siunitx-version-1.cfg
%{_texmfdistdir}/tex/latex/siunitx/siunitx.sty
%doc %{_texmfdistdir}/doc/latex/siunitx/README
%doc %{_texmfdistdir}/doc/latex/siunitx/siunitx.pdf
#- source
%doc %{_texmfdistdir}/source/latex/siunitx/siunitx.dtx
%doc %{_texmfdistdir}/source/latex/siunitx/siunitx.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.5g-1
+ Revision: 812877
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.5c-1
+ Revision: 805077
- Update to latest release.

* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4n-1
+ Revision: 790737
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4j-1
+ Revision: 770282
- Update to latest upstream package

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4h-1
+ Revision: 762726
- Update to latest upstream package

* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4f-1
+ Revision: 759065
- Update to latest upstream release

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4e-2
+ Revision: 756046
- Rebuild to reduce used resources

* Sat Dec 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.4e-1
+ Revision: 743318
- texlive-siunitx

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.4b-1
+ Revision: 739876
- texlive-siunitx

* Tue Nov 22 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.4-1
+ Revision: 732611
- texlive-siunitx

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.3h-1
+ Revision: 719543
- texlive-siunitx
- texlive-siunitx
- texlive-siunitx
- texlive-siunitx

