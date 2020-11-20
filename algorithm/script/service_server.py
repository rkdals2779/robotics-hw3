#!/usr/bin/env python
import rospy
from common_msgs.srv import BatteryNum, BatteryNumRequest

def service_callback(request):
    response = BatteryNumResponse(sum=request.a + request.b)
    print "Charged battery:", request.b, "%", "Battery:", response.sum, "%"
    if response.sum == 100:
        print "Charging Complete"
    return response

    print "Charging Complete"
rospy.init_node('service_server')
service = rospy.Service('charging_battery', BatteryNum, service_callback)
rospy.spin()
