Name:           ros-kinetic-rosserial-test
Version:        0.7.6
Release:        0%{?dist}
Summary:        ROS rosserial_test package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       gtest-devel
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rosserial-client
Requires:       ros-kinetic-rosserial-msgs
Requires:       ros-kinetic-rosserial-python
Requires:       ros-kinetic-rosserial-server
Requires:       ros-kinetic-rostest
Requires:       ros-kinetic-std-msgs
BuildRequires:  gtest-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rosserial-client
BuildRequires:  ros-kinetic-rosserial-msgs
BuildRequires:  ros-kinetic-rosserial-python
BuildRequires:  ros-kinetic-rosserial-server
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-std-msgs

%description
A specialized harness which allows end-to-end integration testing of the
rosserial client and server components.

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
* Wed Mar 01 2017 Mike Purvis <mpurvis@clearpath.ai> - 0.7.6-0
- Autogenerated by Bloom

* Tue Nov 22 2016 Mike Purvis <mpurvis@clearpath.ai> - 0.7.5-0
- Autogenerated by Bloom

* Wed Sep 21 2016 Mike Purvis <mpurvis@clearpath.ai> - 0.7.4-0
- Autogenerated by Bloom

