Name:		texlive-bundledoc
Version:	3.1
Release:	1
Summary:	Bundle together all the files needed to build a LaTeX document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/bundledoc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bundledoc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bundledoc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-bundledoc.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The bundledoc package is a post-processor for the snapshot
package that bundles together all the classes, packages and
files needed to build a given LaTeX document. It reads the .dep
file that snapshot produces, finds each of the files mentioned
therein, and archives them into a single .tar.gz (or .zip, or
whatever) file, suitable for moving across systems,
transmitting to a colleague, etc. A script, arlatex, provides
an alternative "archiving" mechanism, creating a single LaTeX
file that contains all of the ancillary files of a LaTeX
document, together with the document itself, using the
filecontents* environment.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/arlatex
%{_bindir}/bundledoc
%{_texmfdistdir}/scripts/bundledoc/arlatex
%{_texmfdistdir}/scripts/bundledoc/bundledoc
%{_texmfdistdir}/tex/latex/bundledoc/miktex.cfg
%{_texmfdistdir}/tex/latex/bundledoc/texlive-unix.cfg
%doc %{_texmfdistdir}/doc/support/bundledoc/README
%doc %{_mandir}/man1/arlatex.1*
%doc %{_texmfdir}/doc/man/man1/arlatex.man1.pdf
%doc %{_mandir}/man1/bundledoc.1*
%doc %{_texmfdir}/doc/man/man1/bundledoc.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/bundledoc/arlatex arlatex
    ln -sf %{_texmfdistdir}/scripts/bundledoc/bundledoc bundledoc
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
