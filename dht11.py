import dht
import machine

d = dht.DHT11(machine.Pin(40))
d.measure()  # 先调用测量函数
d.temperature()  # 然后可以查湿度
d.humidity()  # 和湿度了