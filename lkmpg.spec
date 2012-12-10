%define name lkmpg
%define version 1.1.0
%define release %mkrel 16

Summary: The Linux Kernel Module Programming Guide 
Name: %{name}
Version: %{version}
Release: %{release}
Group: Books/Computer books
Source: lkmpg.tar.bz2
License: GPL
Buildroot: %{_tmppath}/%{name}-buildroot
BuildArchitectures: noarch
URL: http://www.linuxdoc.org/LDP/lkmpg/mpg.html

%description
This document is for people who want to write kernel modules.

Examples are include.

%prep
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_docdir}/LDP
cd $RPM_BUILD_ROOT%{_docdir}/LDP
bzcat %{SOURCE0} | tar xv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_docdir}/LDP/*




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-16mdv2011.0
+ Revision: 620246
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1.0-15mdv2010.0
+ Revision: 429860
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0-14mdv2009.0
+ Revision: 251243
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.1.0-12mdv2008.1
+ Revision: 140932
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jan 15 2007 Lenny Cartier <lenny@mandriva.com> 1.1.0-12mdv2007.0
+ Revision: 109158
- Rebuild
- Import lkmpg

