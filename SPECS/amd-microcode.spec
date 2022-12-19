# Citrix does not publish SRPMs for their package, so we're duplicating efforts
%define xs_release 1 
%define xs_dist xs8

Summary:        AMD Microcode
Name:           amd-microcode
Version:        20220930
Release:        %{xs_release}%{?dist}
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
* Mon Dec 19 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 20220930-1
- Update to 20220930

* Thu Oct 06 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 20220411-1
- Create amd-microcode RPM
