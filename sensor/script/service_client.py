#!/usr/bin/env python
import rospy
import random
from common_msgs.srv import BatteryNum, BatteryNumRequest

rospy.init_node('service_client')
rospy.wait_for_service('charging_battery')
requester = rospy.ServiceProxy('charging_battery', BatteryNum)

print "requester type:", type(requester), ", callable?", callable(requester)
rate = rospy.Rate(10)
count = 0
originalbattery = random.randint(1,100)
print "Early battery", originalbattery, "%"
while count < 100:
    if count % 1 == 0:
        req = BatteryNumRequest(a=originalbattery, b=count)
        res = requester(req)
        print "Charge amount:", req.b,"%", "Current battery:", res.sum, "%"
    if res.sum == 100:
        print "Charging Complete"
        count = 100
    rate.sleep()
    count += 1
