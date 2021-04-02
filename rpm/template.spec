%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-rosserial-server
Version:        0.9.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rosserial_server package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-thread
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rosserial-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-topic-tools
BuildRequires:  boost-devel
BuildRequires:  python3-devel
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rosserial-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-topic-tools
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
A more performance- and stability-oriented server alternative implemented in C++
to rosserial_python.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri Apr 02 2021 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.9.2-1
- Autogenerated by Bloom

* Wed Sep 09 2020 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.9.1-1
- Autogenerated by Bloom

* Tue Aug 25 2020 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.9.0-1
- Autogenerated by Bloom

