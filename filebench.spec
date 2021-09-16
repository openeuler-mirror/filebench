Name:           filebench
Version:        1.4.9.1
Release:        3
Summary:        A model based file system workload generator

License:        CDDL-1.0
URL:            http://github.com/filebench
Source0:        https://github.com/filebench/filebench/archive/refs/tags/%{version}.tar.gz

Patch1:		0001-filebench-fix-coredump-problem-with-dirwidth-1.patch 

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: gcc
BuildRequires: flex
BuildRequires: bison
BuildRequires: make

%description
Filebench is a file system and storage benchmark that allows to generate a
high variety of workloads. It employs extensive Workload Model Language (WML)
for detailed workload specification.


%prep
%autosetup -p 1


%build
libtoolize
aclocal
autoheader
automake --add-missing
autoconf
%configure
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc AUTHORS ChangeLog COPYING LICENSE NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}


%changelog
* Sat Jul 24 2021 Zhiqiang Liu <liuzhiqiang26@huawei.com> 1.4.9.1-3
- fix one coredump problem with dirwidth=1

* Wed Jul 07 2021 wangxiaomeng <wangxiaomeng@kylinos.cn> 1.4.9.1-2
- chang to autosetup

* Tue Jun 29 2021 sunligang <sunligang@kylinos.cn> 1.4.9.1-1 
- initial package
