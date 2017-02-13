Name:           ros-jade-jsk-footstep-controller
Version:        0.1.11
Release:        1%{?dist}
Summary:        ROS jsk_footstep_controller package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-diagnostic-msgs
Requires:       ros-jade-diagnostic-updater
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-genmsg
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-jsk-footstep-msgs
Requires:       ros-jade-jsk-footstep-planner
Requires:       ros-jade-jsk-pcl-ros
Requires:       ros-jade-jsk-topic-tools
Requires:       ros-jade-kdl-conversions
Requires:       ros-jade-kdl-parser
Requires:       ros-jade-message-filters
Requires:       ros-jade-message-generation
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-sound-play
Requires:       ros-jade-std-msgs
Requires:       ros-jade-tf
Requires:       ros-jade-tf-conversions
Requires:       ros-jade-tf2
Requires:       ros-jade-urdf
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-diagnostic-msgs
BuildRequires:  ros-jade-diagnostic-updater
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-genmsg
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-jsk-footstep-msgs
BuildRequires:  ros-jade-jsk-footstep-planner
BuildRequires:  ros-jade-jsk-pcl-ros
BuildRequires:  ros-jade-jsk-topic-tools
BuildRequires:  ros-jade-kdl-conversions
BuildRequires:  ros-jade-kdl-parser
BuildRequires:  ros-jade-message-filters
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-tf-conversions
BuildRequires:  ros-jade-tf2
BuildRequires:  ros-jade-urdf

%description
The jsk_footstep_controller package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Feb 14 2017 Ryohei Ueda <garaemon@gmail.com> - 0.1.11-1
- Autogenerated by Bloom

