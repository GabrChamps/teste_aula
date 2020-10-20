import rospy
from std_msgs.msg import String

rospy.init_node('Test3')

def timerCallBack(event):
    msg = String()
    msg.data = 'Teste'
    pub.publish(msg)

pub = rospy.Publisher('/topic1', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)

rospy.spin()
