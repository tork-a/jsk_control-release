Name:           ros-hydro-jsk-teleop-joy
Version:        0.1.6
Release:        1%{?dist}
Summary:        ROS jsk_teleop_joy package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_teleop_joy
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-diagnostic-msgs
Requires:       ros-hydro-diagnostic-updater
Requires:       ros-hydro-image-view2
Requires:       ros-hydro-interactive-markers
Requires:       ros-hydro-joy-mouse
Requires:       ros-hydro-jsk-footstep-msgs
Requires:       ros-hydro-jsk-interactive-marker
Requires:       ros-hydro-jsk-rviz-plugins
Requires:       ros-hydro-ps3joy
Requires:       ros-hydro-tf
Requires:       ros-hydro-view-controller-msgs
Requires:       ros-hydro-visualization-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-diagnostic-msgs
BuildRequires:  ros-hydro-diagnostic-updater
BuildRequires:  ros-hydro-interactive-markers
BuildRequires:  ros-hydro-joy-mouse
BuildRequires:  ros-hydro-jsk-footstep-msgs
BuildRequires:  ros-hydro-jsk-interactive-marker
BuildRequires:  ros-hydro-jsk-rviz-plugins
BuildRequires:  ros-hydro-ps3joy
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-view-controller-msgs
BuildRequires:  ros-hydro-visualization-msgs

%description
jsk_teleop_joy

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Jun 19 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.6-1
- Autogenerated by Bloom

* Fri Jun 19 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.6-0
- Autogenerated by Bloom

* Thu Jan 08 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.5-0
- Autogenerated by Bloom

* Sat Oct 11 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.3-0
- Autogenerated by Bloom

* Thu Sep 04 2014 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.1-0
- Autogenerated by Bloom

