Name:           ros-hydro-jsk-ik-server
Version:        0.1.3
Release:        0%{?dist}
Summary:        ROS jsk_ik_server package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_ik_server
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-cmake-modules
Requires:       ros-hydro-mk
Requires:       ros-hydro-moveit-msgs
Requires:       ros-hydro-roseus
Requires:       ros-hydro-rostest
Requires:       ros-hydro-tf
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-mk
BuildRequires:  ros-hydro-moveit-msgs
BuildRequires:  ros-hydro-roseus
BuildRequires:  ros-hydro-rostest
BuildRequires:  ros-hydro-tf

%description
jsk_ik_server

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sat Oct 11 2014 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 0.1.3-0
- Autogenerated by Bloom

* Thu Sep 04 2014 furuta <furuta@jsk.t.u-tokyo.ac.jp> - 0.1.1-0
- Autogenerated by Bloom

