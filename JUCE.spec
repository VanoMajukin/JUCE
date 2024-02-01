Name: JUCE
Version: 7.0.9
Release: alt1

Summary: A cross-platform C++ application framework for creating desktop and mobile applications
License: GPL-3.0+
Group: Development/C++
Url: https://github.com/juce-framework/JUCE

# Source-url: https://github.com/juce-framework/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Patch: JUCE-7.0.9-fix-juceaide_build-alt.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake make clang gcc-c++
BuildRequires: pipewire-jack-libs-devel
BuildRequires: libalsa-devel ladspa_sdk
BuildRequires: libcurl-devel libfreetype-devel
BuildRequires: libX11-devel libXcursor-devel libXinerama-devel libXrandr-devel libXrender-devel libXext-devel libXcomposite-devel
BuildRequires: libwebkit2gtk-devel
BuildRequires: libGLU-devel libGL-devel

%description
JUCE is an open-source cross-platform C++ application framework for creating high quality desktop and mobile applications, including VST, VST3, AU, AUv3, AAX and LV2 audio plug-ins and plug-in hosts. JUCE can be easily integrated with existing projects via CMake, or can be used as a project generation tool via the Projucer, which supports exporting projects for Xcode (macOS and iOS), Visual Studio, Android Studio, Code::Blocks and Linux Makefiles as well as containing a source code editor.

%package devel
Summary:        A cross-platform C++ application framework for creating desktop and mobile applications
Group: Development/C++
Requires:       %name = %version-%release

%description devel
Header files for JUCE

%prep
%setup
%patch -p1

%build
%cmake -DJUCE_BUILD_EXAMPLES=OFF -DJUCE_BUILD_EXTRAS=OFF -DJUCE_INSTALL_DESTINATION=%_lib/cmake/JUCE-%version
%cmake_build

%install
%cmake_install

install -Dv %buildroot%_bindir/JUCE-%version/juceaide %buildroot%_bindir/
install -Dv %buildroot%_bindir/JUCE-%version/juce_lv2_helper %buildroot%_bindir/
install -Dv %buildroot%_bindir/JUCE-%version/juce_vst3_helper %buildroot%_bindir/

rm -rv %buildroot%_bindir/JUCE-%version

%files
%_bindir/juceaide
%_bindir/juce_lv2_helper
%_bindir/juce_vst3_helper
%_libdir/cmake/JUCE-%version/*.cmake
%_libdir/cmake/JUCE-%version/*.in
%_libdir/cmake/JUCE-%version/*.cpp
%_libdir/cmake/JUCE-%version/*.storyboard
%_libdir/cmake/JUCE-%version/*.nib

%files devel
%_includedir/JUCE-%version



%changelog
* Thu Feb 01 2024 Ivan Mazhukin <vanomj@altlinux.org> 7.0.9-alt1
- Initial build for Alt Sisyphus

