Name:           ros-melodic-rosserial-xbee
Version:        0.8.0
Release:        0%{?dist}
Summary:        ROS rosserial_xbee package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosserial_xbee
Source0:        %{name}-%{version}.tar.gz

Requires:       pyserial
Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-rospy
Requires:       ros-melodic-rosserial-msgs
Requires:       ros-melodic-rosserial-python
BuildRequires:  ros-melodic-catkin

%description
Allows multipoint communication between rosserial nodes connected to an xbee.
All nodes communicate back to a master xbee connected to a computer running ROS.
This software currently only works with Series 1 Xbees. This pkg includes python
code from the python-xbee project: http://code.google.com/p/python-xbee/

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Oct 11 2018 Paul Bouchier <paul.bouchier@gmail.com> - 0.8.0-0
- Autogenerated by Bloom

