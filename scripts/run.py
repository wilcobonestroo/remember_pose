#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from ar_track_alvar_msgs.msg import AlvarMarkers
from ar_track_alvar_msgs.msg import AlvarMarker
from geometry_msgs.msg import PoseStamped

#ar_track_alvar/AlvarMarkers

m = AlvarMarker
found = False # check if we have ever seen a tag

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I see %i markers", len(data.markers))
    if len(data.markers) > 0:
        m = data.markers[0] # Get the first item (marker) from the list
        found = True

    
# This is where the program starts
def run():
    rospy.init_node('run', anonymous=True)
    rospy.loginfo("Starting...")

    # Subscribe to the /ar_pose_marker topic
    rospy.Subscriber("ar_pose_marker", AlvarMarkers, callback)

    pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)
    rate = rospy.Rate(0.5) # Hz
    while not rospy.is_shutdown():
        
        rospy.loginfo("Publishing the remembered pose")

        if found:
            pub.publish(m.pose)

        rate.sleep()

if __name__ == '__main__':
    run()