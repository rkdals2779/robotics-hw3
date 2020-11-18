#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from common_msgs.msg import TimePoint

rospy.init_node('sensor_publisher')
pub = rospy.Publisher('point_msg', TimePoint, queue_size=1)
msg = TimePoint()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.timestamp = rospy.get_rostime()
    second = msg.timestamp.secs%100
    msg.point = Point(x=second*2, y=second*3, z=second*4)
    pub.publish(msg)
    print "publish:", msg.timestamp.secs%100, msg.point.x, msg.point.y, msg.point.z
    rate.sleep()
