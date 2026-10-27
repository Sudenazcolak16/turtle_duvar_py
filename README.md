# 🐢 ROS 2 Duvardan Kaçan Kaplumbağa

Bu proje, ROS 2 ortamında `turtlesim` simülasyonunu kullanarak kaplumbağanın duvar sınırlarına çarpmadan hareket etmesini sağlayan kontrol düğümüdür.

---

## 1. Düğüm İlişkileri (Rqt Graph)
![Rqt Graph](rqt_graph.png)

---

## 2. Konum Verileri (/turtle1/pose)
Kaplumbağanın anlık konum ve yönelim bilgileri dinlenir:
![Pose Çıktısı](pose_ciktisi.png)

---

## 3. Duvar Kontrolü ve Terminal Logları
`get_logger().info()` ile yazdırılan anlık konum ve sınır kontrol logları:
![Duvar Çalışması](duvar_calismasi.png)

---

## 4. Turtlesim Simülasyon Hareketi
Kaplumbağanın sınırlara ulaştığında dönerek alan içinde kalışı:
![Simülasyon Hareketi](hareket.png)

---

## 5. Hız Komutları (/turtle1/cmd_vel)
Kaplumbağaya iletilen `geometry_msgs/msg/Twist` mesajları:
![Cmd Vel Çıktısı](cmd_vel_ciktisi.png)

---

## 🚀 Kurulum ve Çalıştırma

Projeyi kendi ROS 2 çalışma alanınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

```bash
cd ~/ros2_ws
colcon build --packages-select turtle_duvar_py
source install/setup.bash
