Name:           ros-kinetic-jsk-ik-server
Version:        0.1.11
Release:        2%{?dist}
Summary:        ROS jsk_ik_server package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_ik_server
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-cmake-modules
Requires:       ros-kinetic-mk
Requires:       ros-kinetic-moveit-msgs
Requires:       ros-kinetic-roseus
Requires:       ros-kinetic-rostest
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-mk
BuildRequires:  ros-kinetic-moveit-msgs
BuildRequires:  ros-kinetic-roseus
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-tf

%description
jsk_ik_server

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
* Tue Feb 14 2017 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 0.1.11-2
- Autogenerated by Bloom

