# Duvardan Kaçan Kaplumbağa (ROS 2 Python)

Bu proje, ROS 2 üzerinde `turtlesim` simülasyonunu kullanarak kaplumbağanın belirlenen sınırlara çarpmadan duvardan kaçmasını sağlayan bir kontrol düğümüdür.

## Özellikler
- `/turtle1/pose` konusuna abone olarak anlık $X$ ve $Y$ koordinatlarını dinler.
- Kaplumbağa sınırlara ($X, Y \le 1.5$ veya $X, Y \ge 9.5$) yaklaştığında yönünü merkeze çevirerek duvardan kaçar.
- `/turtle1/cmd_vel` konusuna hız ve açısal dönüş mesajları yayınlar.
- Saniyede bir `get_logger().info()` ile anlık konum ve parametre bilgilerini yazdırır.
- Hız ve sınır değerleri dinamik ROS 2 parametresi olarak tanımlanmıştır (Bonus).

---

## Kurulum ve Çalıştırma

Çalışma alanınızı derleyin ve ortamı kaynak olarak ekleyin:

```bash
cd ~/ros2_ws
colcon build --packages-select turtle_duvar_py
source install/setup.bash
