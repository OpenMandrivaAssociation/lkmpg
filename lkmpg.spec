%define name lkmpg
%define version 1.1.0
%define release %mkrel 14

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


