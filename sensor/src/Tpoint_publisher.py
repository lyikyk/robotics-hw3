#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from common_msgs.msg import Tpoint
from common_msgs.srv import SubTwoNum, SubTwoNumRequest

rospy.init_node('Tpoint_publisher')
pub = rospy.Publisher('commom_msgs', Tpoint, queue_size=1)
rospy.wait_for_service('sub_two_number')
requester = rospy.ServiceProxy('sub_two_number', SubTwoNum)
msg = Tpoint()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.custom = rospy.get_rostime()
    second = msg.custom.secs
    msg.point = Point(x=second%4, y=second%7, z=second%5)
    pub.publish(msg)
    print "publish:", msg.custom.secs%60, msg.point.x, msg.point.y, msg.point.z
    
    if count % 10 == 0:
        req = SubTwoNumRequest(a=count, b=count/2)
        res = requester(req)
        print count, "request:", req.a, req.b, "response:", res.sub
    count += 1
    rate.sleep()
