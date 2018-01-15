Name:           ros-kinetic-jsk-calibration
Version:        0.1.14
Release:        0%{?dist}
Summary:        ROS jsk_calibration package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-pr2-msgs
Requires:       ros-kinetic-roseus
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-pr2-msgs
BuildRequires:  ros-kinetic-roseus

%description
The jsk_calibration package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Jan 15 2018 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.14-0
- Autogenerated by Bloom

* Tue Apr 18 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.13-0
- Autogenerated by Bloom

* Wed Feb 22 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.12-0
- Autogenerated by Bloom

* Tue Feb 14 2017 Ryohei Ueda <ueda@jsk.t.u-tokyo.ac.jp> - 0.1.11-2
- Autogenerated by Bloom

