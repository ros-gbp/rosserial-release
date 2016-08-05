Name:           ros-kinetic-rosserial-server
Version:        0.7.3
Release:        0%{?dist}
Summary:        ROS rosserial_server package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rosserial-msgs
Requires:       ros-kinetic-rosserial-python
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-topic-tools
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rosserial-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-topic-tools

%description
The rosserial_server package provides a C++ implementation of the rosserial
server side, serving as a more performance- and stability-oriented alternative
to rosserial_python.

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
* Fri Aug 05 2016 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.7.3-0
- Autogenerated by Bloom

* Mon Jul 18 2016 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.7.2-0
- Autogenerated by Bloom

