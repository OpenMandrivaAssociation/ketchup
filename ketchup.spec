Name: ketchup
Version: 0.9.8
Release:  %mkrel 5
Group: Development/Kernel
Summary: Linux Kernel source switch/update tool
License: GPL
URL: http://www.selenic.com/ketchup/wiki/
Source: http://www.selenic.com/ketchup/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch

Requires: python
Requires: wget
Requires: gnupg

%description
Ketchup is a tool for updating or switching between versions of the
Linux kernel source. It can:
- Find the latest versions of numerous KernelTrees;
- Calculate which patches are needed to move to that version;
- Download any patches or tarballs that aren't cached;
- Check GPG signatures where available;
- Apply and unapply patches to get the desired result.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/contrib
install -m755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m644 ketchup.1 -D $RPM_BUILD_ROOT%{_mandir}/man1/ketchup.1
install -m755 contrib/* -D $RPM_BUILD_ROOT%{_datadir}/%{name}/contrib/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/ketchup
%{_mandir}/man1/ketchup.1.*
%{_datadir}/%{name}/contrib/*



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.8-5mdv2011.0
+ Revision: 619959
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.9.8-4mdv2010.0
+ Revision: 429667
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.9.8-3mdv2009.0
+ Revision: 247739
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.9.8-1mdv2008.1
+ Revision: 136523
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import ketchup


* Thu May 04 2006 Leonardo Chiquitto Filho <chiquitto@mandriva.com> 0.9.8-1mdk
- update to 0.9.8

* Fri Mar 31 2006 Leonardo Chiquitto Filho <chiquitto@mandriva.com> 0.9.6-1mdk
- initial release
