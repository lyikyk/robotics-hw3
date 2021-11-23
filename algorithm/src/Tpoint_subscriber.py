#!/usr/bin/env python
import rospy
from common_msgs.msg import Tpoint

def callback(msg):
    print "subscribe:", msg.custom.secs%60, msg.point.x, msg.point.y, msg.point.z

rospy.init_node('Tpoint_subscriber')
sub = rospy.Subscriber('commom_msgs', Tpoint, callback)
rospy.spin()
