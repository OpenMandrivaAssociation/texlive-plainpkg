%global tl_name plainpkg
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4a
Release:	%{tl_revision}.1
Summary:	A minimal method for making generic packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/plainpkg
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plainpkg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plainpkg.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plainpkg.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a minimal method for making generic (i.e., TeX-
format-independent) packaged, combining maybeload functionality,
fallback definitions for LaTeX \ProvidesPackage and \RequirePackage
functionality, and handling of arbitrary (multiple) "private letters"
(analagous LaTeX packages' use of "@") in nested package files. The
documentation contains a central reference for making and using generic
packages based on the package.

