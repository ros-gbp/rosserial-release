Name:           ros-indigo-rosserial-xbee
Version:        0.6.4
Release:        0%{?dist}
Summary:        ROS rosserial_xbee package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosserial_xbee
Source0:        %{name}-%{version}.tar.gz

Requires:       pyserial
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rosserial-msgs
Requires:       ros-indigo-rosserial-python
BuildRequires:  ros-indigo-catkin

%description
rosserial_xbee provides tools to do point to multipoint communication between
rosserial nodes connected to an xbee. All of the nodes communicate back to a
master xbee connected to a computer running ROS. This software currently only
works with Series 1 Xbees. This pkg includes python code from the python-xbee
project: http://code.google.com/p/python-xbee/

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
* Mon Jul 06 2015 Paul Bouchier <paul.bouchier@gmail.com> - 0.6.4-0
- Autogenerated by Bloom

