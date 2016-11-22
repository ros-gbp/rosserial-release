Name:           ros-kinetic-rosserial-tivac
Version:        0.7.5
Release:        0%{?dist}
Summary:        ROS rosserial_tivac package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rosserial_tivac
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-rosserial-client
Requires:       ros-kinetic-rosserial-msgs
BuildRequires:  ros-kinetic-catkin

%description
rosserial_tivac package provides the required hardware definitions for compiling
rosserial_client targets for TivaC Launchpad evaluation boards.

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
* Tue Nov 22 2016 Vitor Matos <vmatos@robosavvy.com> - 0.7.5-0
- Autogenerated by Bloom

* Wed Sep 21 2016 Vitor Matos <vmatos@robosavvy.com> - 0.7.4-0
- Autogenerated by Bloom

* Fri Aug 05 2016 Vitor Matos <vmatos@robosavvy.com> - 0.7.3-0
- Autogenerated by Bloom

* Mon Jul 18 2016 Vitor Matos <vmatos@robosavvy.com> - 0.7.2-0
- Autogenerated by Bloom

