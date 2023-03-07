#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/rob/UCD_robot_ws_v2/src/universal_robot/ur_kinematics"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/rob/UCD_robot_ws_v2/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/rob/UCD_robot_ws_v2/install/lib/python3/dist-packages:/home/rob/UCD_robot_ws_v2/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/rob/UCD_robot_ws_v2/build" \
    "/usr/bin/python3" \
    "/home/rob/UCD_robot_ws_v2/src/universal_robot/ur_kinematics/setup.py" \
     \
    build --build-base "/home/rob/UCD_robot_ws_v2/build/universal_robot/ur_kinematics" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/rob/UCD_robot_ws_v2/install" --install-scripts="/home/rob/UCD_robot_ws_v2/install/bin"
