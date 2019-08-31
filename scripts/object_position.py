#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from visualization_msgs.msg import Marker, MarkerArray

class Object_position:

    def __init__(self):
        self.sub = rospy.Subscriber("clusters", MarkerArray, self.callback)
        self.r = rospy.Rate(50)
        self.dx = 0
        self.dy = 0

    def callback(self, msg):
        m = msg.markers[0]
        if (m.ns == "target_cluster"):
            self.dx = m.pose.position.x
            self.dy = m.pose.position.y
            rospy.loginfo("Position: [%f, %f]"%(self.dx,self.dy))
 
    def listener(self):
        print(self.dx, self.dy)

if __name__ == '__main__':
    try:
        if not rospy.is_shutdown():
           rospy.init_node("Object_position")
           op = Object_position()
           rospy.spin()
           #op.listener()
    except rospy.ROSInterruptException:
        pass