%global tl_name bundledoc
%global tl_revision 79024

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.6
Release:	%{tl_revision}.1
Summary:	Bundle together all the files needed to build a LaTeX document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/bundledoc
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bundledoc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bundledoc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(bundledoc.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundledoc package is a post-processor for the snapshot package that
bundles together all the classes, packages and files needed to build a
given LaTeX document. It reads the .dep file that snapshot produces,
finds each of the files mentioned therein, and archives them into a
single .tar.gz (or .zip, or whatever) file, suitable for moving across
systems, transmitting to a colleague, etc. A script, arlatex, provides
an alternative "archiving" mechanism, creating a single LaTeX file that
contains all of the ancillary files of a LaTeX document, together with
the document itself, using the filecontents* environment.

