Name:           ros-melodic-rosserial-mbed
Version:        0.8.0
Release:        0%{?dist}
Summary:        ROS rosserial_mbed package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosserial_mbed
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-rospy
Requires:       ros-melodic-rosserial-client
Requires:       ros-melodic-rosserial-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-message-generation

%description
rosserial for mbed platforms.

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
* Thu Oct 11 2018 Gary Servin <garyservin@gmail.com> - 0.8.0-0
- Autogenerated by Bloom

