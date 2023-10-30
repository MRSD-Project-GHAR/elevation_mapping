#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped


def odom_callback(msg):
    pose_msg = PoseWithCovarianceStamped()
    pose_msg.header = msg.header
    pose_msg.pose = msg.pose
    pose_pub.publish(pose_msg)


rospy.init_node('odom_to_pose')
rospy.Subscriber('/rtabmap/odom', Odometry, odom_callback)
pose_pub = rospy.Publisher('/camera_link_pose', PoseWithCovarianceStamped, queue_size=10)
rospy.spin()
