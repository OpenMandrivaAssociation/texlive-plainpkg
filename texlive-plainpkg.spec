# revision 27765
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-plainpkg
Version:	20131018
Release:	4
Summary:	TeXLive plainpkg package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plainpkg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plainpkg.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plainpkg.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive plainpkg package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/plainpkg/plainpkg.tex
%doc %{_texmfdistdir}/doc/generic/plainpkg/README
%doc %{_texmfdistdir}/doc/generic/plainpkg/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/generic/plainpkg/plainpkg-doc.pdf
#- source
%doc %{_texmfdistdir}/source/generic/plainpkg/plainpkg-doc.tex
%doc %{_texmfdistdir}/source/generic/plainpkg/srcfiles.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
