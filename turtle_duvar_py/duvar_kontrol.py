#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class DuvarKontrol(Node):
    def __init__(self):
        super().__init__('turtle_duvar_node')

        self.declare_parameter('hiz', 2.0)
        self.declare_parameter('alt_sinir', 1.5)
        self.declare_parameter('ust_sinir', 9.5)

        self.cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.mevcut_pose = None

    def pose_callback(self, msg: Pose):
        self.mevcut_pose = msg
        alt = self.get_parameter('alt_sinir').value
        ust = self.get_parameter('ust_sinir').value
        hiz = self.get_parameter('hiz').value

        cmd = Twist()

        # Duvar sınır kontrolü
        if msg.x <= alt or msg.x >= ust or msg.y <= alt or msg.y >= ust:
            # Merkeze (5.5, 5.5) olan açıyı hesapla
            merkez_aci = math.atan2(5.54 - msg.y, 5.54 - msg.x)
            aci_farki = merkez_aci - msg.theta

            # Açıyı [-pi, pi] aralığına normalize et
            while aci_farki > math.pi:
                aci_farki -= 2 * math.pi
            while aci_farki < -math.pi:
                aci_farki += 2 * math.pi

            # Yüzünü merkeze çevir ve yavaşça içeri doğru ilerle
            cmd.angular.z = 3.0 * aci_farki
            cmd.linear.x = 1.0
        else:
            # Güvenli alanda normal hızla düz git
            cmd.linear.x = hiz
            cmd.angular.z = 0.0

        self.cmd_vel_pub.publish(cmd)

    def timer_callback(self):
        if self.mevcut_pose is not None:
            hiz = self.get_parameter('hiz').value
            alt = self.get_parameter('alt_sinir').value
            ust = self.get_parameter('ust_sinir').value
            self.get_logger().info(
                f"Konum -> X: {self.mevcut_pose.x:.2f}, Y: {self.mevcut_pose.y:.2f} | Hız: {hiz}, Sınırlar: [{alt}, {ust}]"
            )

def main(args=None):
    rclpy.init(args=args)
    node = DuvarKontrol()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
