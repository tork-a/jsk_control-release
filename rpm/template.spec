Name:           ros-jade-eus-qpoases
Version:        0.1.13
Release:        0%{?dist}
Summary:        ROS eus_qpoases package

Group:          Development/Libraries
License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-euslisp
Requires:       ros-jade-rostest
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-euslisp
BuildRequires:  ros-jade-rostest
BuildRequires:  subversion

%description
eus_qpoases

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
* Tue Apr 18 2017 Shunichi Nozawa <nozawa@jsk.t.u-tokyo.ac.jp> - 0.1.13-0
- Autogenerated by Bloom

* Tue Feb 14 2017 Shunichi Nozawa <nozawa@jsk.t.u-tokyo.ac.jp> - 0.1.11-1
- Autogenerated by Bloom

