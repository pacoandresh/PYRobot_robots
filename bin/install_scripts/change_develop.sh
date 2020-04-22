packages_python="/usr/local/lib/python3.7/dist-packages"
dir_PYRobot=$PWD/PYRobot
dir_PYRobot_cli=$PWD/PYRobot_cli
dir_robots=$PWD/robots/

sudo rm -f $packages_python/PYRobot
sudo ln -s  $dir_PYRobot $packages_python/PYRobot

sudo rm -f $packages_python/PYRobot_cli
sudo ln -s  $dir_PYRobot_cli $packages_python/PYRobot_cli

PYROBOTS=$dir_robots
export PYROBOTS
ls -la $packages_python/PYRobot*

echo $PYROBOTS
cd $PYROBOTS/bin
