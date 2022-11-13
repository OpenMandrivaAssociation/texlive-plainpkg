Name:		texlive-plainpkg
Version:	27765
Release:	1
Summary:	TeXLive plainpkg package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plainpkg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plainpkg.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plainpkg.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
