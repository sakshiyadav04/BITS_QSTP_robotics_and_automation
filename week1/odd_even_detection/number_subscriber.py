#!/usr/bin/env python3
import rospy

from std_msgs.msg import Int32
from std_msgs.msg import String 

def callback(msg):
    if(msg.data %2 == 0):
    	pub1.publish("EVEN")
    else:
    	pub1.publish("ODD")
    

rospy.init_node('number_subscriber')
pub1 = rospy.Publisher('odd_even_classifier',String,queue_size=10)
sub = rospy.Subscriber('integer_generator', Int32, callback)

rospy.spin()
