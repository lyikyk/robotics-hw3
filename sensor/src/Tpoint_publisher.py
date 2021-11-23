#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from common_msgs.msg import Tpoint

rospy.init_node('Tpoint_publisher')
pub = rospy.Publisher('commom_msgs', Tpoint, queue_size=1)
msg = Tpoint()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.custom = rospy.get_rostime()
    second = msg.custom.secs
    msg.point = Point(x=second%4, y=second%7, z=second%5)
    pub.publish(msg)
    print "publish:", msg.custom.secs%60, msg.point.x, msg.point.y, msg.point.z
    rate.sleep()
