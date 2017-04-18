Name:           ros-kinetic-jsk-footstep-controller
Version:        0.1.13
Release:        0%{?dist}
Summary:        ROS jsk_footstep_controller package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-diagnostic-msgs
Requires:       ros-kinetic-diagnostic-updater
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-genmsg
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-jsk-footstep-msgs
Requires:       ros-kinetic-jsk-footstep-planner
Requires:       ros-kinetic-jsk-pcl-ros
Requires:       ros-kinetic-jsk-topic-tools
Requires:       ros-kinetic-kdl-conversions
Requires:       ros-kinetic-kdl-parser
Requires:       ros-kinetic-message-filters
Requires:       ros-kinetic-message-generation
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-sound-play
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-tf-conversions
Requires:       ros-kinetic-tf2
Requires:       ros-kinetic-urdf
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-diagnostic-msgs
BuildRequires:  ros-kinetic-diagnostic-updater
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-genmsg
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-jsk-footstep-msgs
BuildRequires:  ros-kinetic-jsk-footstep-planner
BuildRequires:  ros-kinetic-jsk-pcl-ros
BuildRequires:  ros-kinetic-jsk-topic-tools
BuildRequires:  ros-kinetic-kdl-conversions
BuildRequires:  ros-kinetic-kdl-parser
BuildRequires:  ros-kinetic-message-filters
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-tf-conversions
BuildRequires:  ros-kinetic-tf2
BuildRequires:  ros-kinetic-urdf

%description
The jsk_footstep_controller package

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
* Tue Apr 18 2017 Ryohei Ueda <garaemon@gmail.com> - 0.1.13-0
- Autogenerated by Bloom

* Wed Feb 22 2017 Ryohei Ueda <garaemon@gmail.com> - 0.1.12-0
- Autogenerated by Bloom

* Tue Feb 14 2017 Ryohei Ueda <garaemon@gmail.com> - 0.1.11-2
- Autogenerated by Bloom

