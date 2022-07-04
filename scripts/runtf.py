#!/usr/bin/env python
import tf
import rospy

# TF -> in eerste instantie wachten op usb_cam
# ar_alvar published in usb_cam frame
# wij luisteren daar naar
#   eventueel beslissen of tag mooi in het midden ligt
#   Als wij er een horen,
#     Vragen om 'tag frame in odom' / ar_marker_2 is de naam van het TF frame
#     deze blijven wij publishen op odom frame



def run():

    rospy.init_node('persistent_tf_publisher')
    listener = tf.TransformListener()
    broadcaster = tf.TransformBroadcaster()

    found = False # Check if we have seen a tag
    trans = (0,0,0)
    rot = (0,0,0)

    rate = rospy.Rate(0.5)

    while not rospy.is_shutdown():
        # Listen
        try:
            print("Looking up the TF tranform in odom frame")
            (trans,rot) = listener.lookupTransform('/odom', '/ar_marker_2', rospy.Time(0))
            print("found TF, updating the location to be remembered")

            found = True

        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print("Could not find transform from camera to ar marker")

        #Broadcast
        if found:
            print ("Broadcasting the remembered location")
            broadcaster.sendTransform((trans[0], trans[1], trans[2]),
                tf.transformations.quaternion_from_euler(rot[0], rot[1], rot[2]),
                rospy.Time.now(),
                "persistant_tag_frame", # name of the frame that was remembered.
                "odom")
        else:
            print("The marker was not seen yet, so nothing to publish")

        rate.sleep()
        print()

if __name__ == '__main__':
    run()
