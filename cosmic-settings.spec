%undefine _debugsource_packages

%define         appname com.system76.CosmicSettings
Name:           cosmic-settings
Version:        1.0.0
Release:        0.alpha5.0
Summary:        COSMIC Settings
License:        GPL-3.0-only
Group:          Utility/COSMIC
URL:            https://github.com/pop-os/cosmic-settings
Source0:        https://github.com/pop-os/cosmic-settings/archive/epoch-%{version}-alpha.5/%{name}-epoch-%{version}-alpha.5.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  clang-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  llvm-devel
BuildRequires:  mold
BuildRequires:  pkgconfig
BuildRequires:  polkit
BuildRequires:  rust >= 1.80
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       cosmic-randr
Requires:       cosmic-settings-daemon

Requires:       accountsservice
Requires:       iso-codes
Requires:       gettext
Requires:       x11-data-xkbdata

Recommends:  adw-gtk3

%description
The settings application for the COSMIC desktop environment. Developed with
libcosmic, using the iced GUI library.

%prep
%autosetup -n %{name}-epoch-%{version}-alpha.5 -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/applications/%{appname}.{About,Appearance,Bluetooth,DateTime,DefaultApps,Desktop,Displays,Dock,Firmware,Input,Power,Keyboard,Mouse,Network,Notifications,Panel,RegionLanguage,Sound,System,Time,Touchpad,Users,Vpn,Wallpaper,WindowManagement,Wired,Wireless,Workspaces}.desktop
%{_datadir}/cosmic
%{_datadir}/icons/hicolor/??x??/apps/%{appname}.svg
%{_datadir}/icons/hicolor/???x???/apps/%{appname}.svg
%{_datadir}/icons/hicolor/scalable/status/*.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_datadir}/polkit-1/rules.d/cosmic-settings.rules
%{_datadir}/polkit-1/actions/com.system76.CosmicSettings.Users.policy
