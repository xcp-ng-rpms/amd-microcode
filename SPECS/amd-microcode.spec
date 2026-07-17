# Citrix does not publish SRPMs for their package, so we're duplicating efforts
%define xs_release 1
%define xs_dist xs8

Summary:        AMD Microcode
Name:           amd-microcode
# The version number is that of linux-firmware
Version:        20260519
Release:        %{xs_release}.1%{?dist}
License:        Redistributable
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git

# Source tarball created with `rpm2archive amd-microcode-%{version}-%{xs_release}-%{xs_dist}.noarch.rpm`
Source0:        %{name}-%{version}-%{xs_release}.%{xs_dist}.noarch.rpm.tgz

BuildArch:      noarch
BuildRequires:  kernel-devel

%description
Microcode blobs for AMD CPUs.  This is a subset of linux-firmware.git

%prep
%setup -q -c

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
* Fri Jul 17 2026 Gael Duperrey <gduperrey@vates.fr> - 20260519-1.1
- Update to 2026-05-19 drop as redistributed by XenServer
  Updated CPUs:
    BRH-C1 00b00f21: 2025-10-17, rev 0b002161 -> 2025-10-17, rev 0b002162
   BRHD-B0 00b10f10: 2025-10-17, rev 0b101058 -> 2025-10-17, rev 0b101059

* Mon Dec 08 2025 Thierry Escande <thierry.escande@vates.tech> - 20251203-1.1
- Update to the 2025-12-03 drop as redistributed by XenServer
  New CPUs:
     BRH-C1 00b00f21: 2025-10-17, rev 0b002161
     SHP-C1 00b00f81: 2025-10-20, rev 0b008121
    BRHD-B0 00b10f10: 2025-10-17, rev 0b101058
     STX-B0 00b20f40: 2025-10-19, rev 0b204037
     GNR-B0 00b40f40: 2025-10-20, rev 0b404035
     GNR-B1 00b40f41: 2025-10-20, rev 0b404108
     KRK-A0 00b60f00: 2025-10-19, rev 0b600037
    KRK2-A0 00b60f80: 2025-10-19, rev 0b608038
    STXH-A0 00b70f00: 2025-10-19, rev 0b700037
  Secondary blobs on existing CPUs:
      GN-B1 00a00f11: 2025-04-18, rev 0a0011de
      GN-B2 00a00f12: 2025-03-27, rev 0a001247
      RS-B1 00a10f11: 2025-06-09, rev 0a101158
      RS-B2 00a10f12: 2025-06-12, rev 0a101253
    RSDN-A2 00aa0f02: 2025-06-12, rev 0aa0021c

* Thu Jul 10 2025 Gael Duperrey <gduperrey@vates.fr> - 20250626-1.1
- Update to 20250626-1 as redistributed by XenServer
- Updated CPUs:
    GN-B1 00a00f11: 2024-02-23, rev 0a0011d5 -> 2024-09-06, rev 0a0011d7
    GN-B2 00a00f12: 2024-02-26, rev 0a001238 -> 2024-09-06, rev 0a00123b
   CGL-B2 00a00f82: 2024-02-29, rev 0a00820c -> 2024-09-13, rev 0a00820d
    RS-B1 00a10f11: 2024-02-23, rev 0a101148 -> 2024-09-06, rev 0a10114c
    RS-B2 00a10f12: 2024-02-26, rev 0a101248 -> 2024-09-06, rev 0a10124c
   STP-B1 00a10f81: 2024-02-27, rev 0a108108 -> 2024-09-11, rev 0a108109
   VMR-B0 00a20f10: 2024-08-27, rev 0a20102d -> 2024-09-13, rev 0a20102e
   VMR-B2 00a20f12: 2024-02-29, rev 0a201210 -> 2024-09-13, rev 0a201211
   RMB-B1 00a40f41: 2024-02-29, rev 0a404107 -> 2024-09-13, rev 0a404108
   CZN-A0 00a50f00: 2024-02-29, rev 0a500011 -> 2024-09-13, rev 0a500012
   RPL-B2 00a60f12: 2024-02-27, rev 0a601209 -> 2024-09-11, rev 0a60120a
   PHX-A1 00a70f41: 2024-02-28, rev 0a704107 -> 2024-09-11, rev 0a704108
  HPT1-A2 00a70f52: 2024-02-28, rev 0a705206 -> 2024-09-11, rev 0a705208
  PHX2-A0 00a70f80: 2024-02-28, rev 0a708007 -> 2024-09-11, rev 0a708008
  HPT2-A0 00a70fc0: 2024-02-28, rev 0a70c005 -> 2024-09-11, rev 0a70c008
  RSDN-A2 00aa0f02: 2024-02-28, rev 0aa00215 -> 2024-09-06, rev 0aa00216

* Fri Apr 18 2025 Samuel Verschelde <stormi-xcp@ylix.fr> - 20241121-1.1
- Packaging fix.
- Remove overridden amd_fam17h and amd_fam19h files introduced in 20240503-1.1 build
  as we now get these directly from the "source" tarball.

* Wed Feb 12 2025 Samuel Verschelde <stormi-xcp@ylix.fr> - 20241121-1
- Update to 20241121-1

* Wed Nov 27 2024 David Morel <david.morel@vates.tech> - 20240503-1.1
- Update microcode for amd_fam17h and amd_fam19h from upsteam 2024-11-21 drop

* Wed Jun 19 2024 Samuel Verschelde <stormi-xcp@ylix.fr> - 20240503-1
- Update to 20240503-1

* Tue Jan 23 2024 Samuel Verschelde <stormi-xcp@ylix.fr> - 20231205-1
- Update to 20231205-1

* Tue Sep 19 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 20230725-1
- Update to 20230725-1
- This brings us back in sync with XenServer 8

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
