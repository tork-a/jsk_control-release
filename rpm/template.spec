Name:           ros-indigo-joy-mouse
Version:        0.1.8
Release:        0%{?dist}
Summary:        ROS joy_mouse package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       python-pyudev
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
BuildRequires:  python-pyudev
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-sensor-msgs

%description
The joy_mouse package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Nov 02 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.8-0
- Autogenerated by Bloom

* Sun Nov 01 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.7-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.6-0
- Autogenerated by Bloom

* Fri Feb 13 2015 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.5-0
- Autogenerated by Bloom

