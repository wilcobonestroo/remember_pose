# Remeber_pose

Demo code to listen to updates from ar_tag_alvar messages and remember and republish the pose. The package is written for ROS Noetic.

Make sure to run the alvar detection with something like:

`rosrun ar_track_alvar individualMarkersNoKinect _image_size:=5 _output_frame:=odom`

I used the package [Gazebo Models](https://github.com/mikaelarguedas/gazebo_models) to generate AR tags that can be used in Gazebo.

I used the simulation package from Turtlebot to have a simulation with a camera. Start it with:

`roslaunch turtlebot3_gazebo turtlebot3_world.launch`

Moreover, I used the launch file from the same package to launch RVIZ:

`roslaunch turtlebot3_gazebo turtlebot3_gazebo_rviz.launch`

As I could not run the official ar tag code in Noetic, I used the repo that was described at the end of [this issue](https://github.com/ros-perception/ar_track_alvar/issues/82). 

`git clone https://github.com/machinekoder/ar_track_alvar.git -b noetic-devel`

## Usage

Just clone this repo into the `src` folder of your workpackage and build it with `catkin_make`.

`git clone https://github.com/wilcobonestroo/remember_pose.git`
