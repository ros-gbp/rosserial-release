Name:           ros-jade-rosserial-mbed
Version:        0.7.5
Release:        0%{?dist}
Summary:        ROS rosserial_mbed package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosserial_mbed
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-message-runtime
Requires:       ros-jade-rospy
Requires:       ros-jade-rosserial-client
Requires:       ros-jade-rosserial-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-message-generation

%description
Libraries and examples for ROSserial usage on Mbed Platforms.

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
* Tue Nov 22 2016 Gary Servin <garyservin@gmail.com> - 0.7.5-0
- Autogenerated by Bloom

* Wed Sep 21 2016 Gary Servin <garyservin@gmail.com> - 0.7.4-0
- Autogenerated by Bloom

* Fri Aug 05 2016 Gary Servin <garyservin@gmail.com> - 0.7.3-0
- Autogenerated by Bloom

* Fri Jul 15 2016 Gary Servin <garyservin@gmail.com> - 0.7.2-0
- Autogenerated by Bloom

