# Citrix does not publish SRPMs for their package, so we're duplicating efforts
%define xs_release 2
%define xs_dist xs8

Summary:        AMD Microcode
Name:           amd-microcode
# The version number is that of linux-firmware
Version:        20220930
Release:        %{xs_release}.2%{?dist}
License:        Redistributable
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git

# Source tarball created with `rpm2archive amd-microcode-%{version}-%{xs_release}-%{xs_dist}.noarch.rpm`
Source0:        %{name}-%{version}-%{xs_release}.%{xs_dist}.noarch.rpm.tgz
# Temporarily override some files from recent upstream releases to fix security issues
# FIXME: to be removed once Source0 is updated again.
Source1: microcode_amd_fam17h.bin
Source2: microcode_amd_fam19h.bin

BuildArch:      noarch
BuildRequires:  kernel-devel

%description
Microcode blobs for AMD CPUs.  This is a subset of linux-firmware.git

%prep
%setup -q -c
cp %{SOURCE1} %{SOURCE2} lib/firmware/amd-ucode/

%build

%install
mkdir -p %{buildroot}/lib/firmware/amd-ucode
install -m 644 lib/firmware/amd-ucode/* %{buildroot}/lib/firmware/amd-ucode

%post
%{regenerate_initrd_post}

%postun
%{regenerate_initrd_postun}

%posttrans
%{regenerate_initrd_posttrans}

%clean
rm -rf %{buildroot}

%files
%license usr/share/licenses/%{name}-%{version}/*
%doc usr/share/doc/%{name}-%{version}/*
/lib/firmware/amd-ucode

%changelog
* Tue Aug 22 2023 Gael Duperrey <gduperrey@vates.fr> - 20220930-2.2
- Update microcode for amd_fam19h

* Thu Jul 27 2023 Gael Duperrey <gduperrey@vates.fr> - 20220930-2.1
- Update microcode for XSA-433 from XS82ECU1041

* Fri Mar 17 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 20220930-2
- Update to the 20230131 drop.
- Updated CPUs:
    GN-A1 00a00f10: 2022-09-01, rev 0a001075 -> 2023-01-17, rev 0a001078
    GN-B1 00a00f11: 2022-08-30, rev 0a0011a8 -> 2023-01-14, rev 0a0011ce
    GN-B2 00a00f12: 2022-08-30, rev 0a00122e -> 2023-01-17, rev 0a001231

* Mon Dec 19 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 20220930-1
- Update to 20220930

* Thu Oct 06 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 20220411-1
- Create amd-microcode RPM
