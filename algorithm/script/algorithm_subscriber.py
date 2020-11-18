#!/usr/bin/env python
import rospy
from common_msgs.msg import TimePoint

def callback(msg):
    print "subscribe:", msg.timestamp.secs%100, msg.point.x, msg.point.y, msg.point.z

rospy.init_node('algorithm_subscriber')
sub = rospy.Subscriber('point_msg', TimePoint, callback)
rospy.spin()
