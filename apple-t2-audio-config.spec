Name:           apple-t2-audio-config

Version:        1
Release:        1%{?dist}.1
Summary:        Audio configuration files for Apple T2 Macs

Source0:        91-pulseaudio-custom.rules
Source1:        apple-t2.conf
Source2:        AppleT2.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%description
Audio configuration files for Apple T2 Macs using the apple_bce driver

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/alsa/cards/ $RPM_BUILD_ROOT/usr/share/alsa-card-profile/mixer/profile-sets/ $RPM_BUILD_ROOT/usr/lib/udev/rules.d/
install -pm 0644 %SOURCE0 $RPM_BUILD_ROOT/usr/lib/udev/rules.d/91-pulseaudio-custom.rules
install -pm 0644 %SOURCE1 $RPM_BUILD_ROOT/usr/share/alsa-card-profile/mixer/profile-sets/apple-t2.conf
install -pm 0644 %SOURCE2 $RPM_BUILD_ROOT/usr/share/alsa/cards/AppleT2.conf

%files
/usr/share/alsa/cards/AppleT2.conf
/usr/share/alsa-card-profile/mixer/profile-sets/apple-t2.conf
/usr/lib/udev/rules.d/91-pulseaudio-custom.rules

%clean
rm -rf $RPM_BUILD_ROOT

# TODO: Make packages for edge cases, see:
# https://gist.github.com/bigbadmonster17/8b670ae29e0b7be2b73887f3f37a057b
# https://gist.github.com/kevineinarsson/8e5e92664f97508277fefef1b8015fba