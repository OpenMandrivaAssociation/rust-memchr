%bcond_without check
%global debug_package %{nil}

%global crate memchr

Name:           rust-memchr
Version:        2.5.0
Release:        1
Summary:        Safe interface to memchr

# Upstream license specification: Unlicense/MIT
License:        Unlicense OR MIT
URL:            https://crates.io/crates/memchr
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21
%if %{with check}
BuildRequires:  (crate(quickcheck) >= 1.0.3 with crate(quickcheck) < 2.0.0~)
%endif

%global _description %{expand:
Safe interface to memchr.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(memchr) = 2.5.0
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(memchr/default) = 2.5.0
Requires:       cargo
Requires:       crate(memchr) = 2.5.0
Requires:       crate(memchr/std) = 2.5.0

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+compiler_builtins-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(memchr/compiler_builtins) = 2.5.0
Requires:       (crate(compiler_builtins/default) >= 0.1.2 with crate(compiler_builtins/default) < 0.2.0~)
Requires:       cargo
Requires:       crate(memchr) = 2.5.0

%description -n %{name}+compiler_builtins-devel %{_description}

This package contains library source intended for building other packages which
use the "compiler_builtins" feature of the "%{crate}" crate.

%files       -n %{name}+compiler_builtins-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+core-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(memchr/core) = 2.5.0
Requires:       (crate(rustc-std-workspace-core/default) >= 1.0.0 with crate(rustc-std-workspace-core/default) < 2.0.0~)
Requires:       cargo
Requires:       crate(memchr) = 2.5.0

%description -n %{name}+core-devel %{_description}

This package contains library source intended for building other packages which
use the "core" feature of the "%{crate}" crate.

%files       -n %{name}+core-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+libc-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(memchr/libc) = 2.5.0
Requires:       (crate(libc) >= 0.2.18 with crate(libc) < 0.3.0~)
Requires:       cargo
Requires:       crate(memchr) = 2.5.0

%description -n %{name}+libc-devel %{_description}

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%files       -n %{name}+libc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rustc-dep-of-std-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(memchr/rustc-dep-of-std) = 2.5.0
Requires:       cargo
Requires:       crate(memchr) = 2.5.0
Requires:       crate(memchr/compiler_builtins) = 2.5.0
Requires:       crate(memchr/core) = 2.5.0

%description -n %{name}+rustc-dep-of-std-devel %{_description}

This package contains library source intended for building other packages which
use the "rustc-dep-of-std" feature of the "%{crate}" crate.

%files       -n %{name}+rustc-dep-of-std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(memchr/std) = 2.5.0
Requires:       cargo
Requires:       crate(memchr) = 2.5.0

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+use_std-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(memchr/use_std) = 2.5.0
Requires:       cargo
Requires:       crate(memchr) = 2.5.0
Requires:       crate(memchr/std) = 2.5.0

%description -n %{name}+use_std-devel %{_description}

This package contains library source intended for building other packages which
use the "use_std" feature of the "%{crate}" crate.

%files       -n %{name}+use_std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
