#!/usr/bin/env python3
import rospy
import random
from std_msgs.msg import Int32


rospy.init_node('number_publisher') # node name

pub = rospy.Publisher('integer_generator', Int32,queue_size = 10) #pub is a object, integer_generator -> topic name
rate = rospy.Rate(2)

count = 0

while not rospy.is_shutdown():
    count = random.randint(0,1000)
    pub.publish(count)
    
    rate.sleep()
