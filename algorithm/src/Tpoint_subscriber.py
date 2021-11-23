#!/usr/bin/env python
import rospy
from common_msgs.msg import Tpoint
from common_msgs.srv import SubTwoNum, SubTwoNumResponse


def callback(msg):
    print "subscribe:", msg.custom.secs%60, msg.point.x, msg.point.y, msg.point.z

def service_callback(request):
    response = AddTwoNumResponse(sub=request.a - request.b)
    print "request data:", request.a, request.b, ", response:", response.sub
    return response

rospy.init_node('Tpoint_subscriber')
sub = rospy.Subscriber('commom_msgs', Tpoint, callback)
service = rospy.Service('sub_two_number', SubTwoNum, service_callback)
rospy.spin()
