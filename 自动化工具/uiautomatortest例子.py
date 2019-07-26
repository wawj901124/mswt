import uiautomator2 as u2
from time import sleep

d = u2.connect('810EBM32TZ4K')  #d = u2.connect('192.168.8.100') 既可以通过设备名称连接也可以通过设备wifi(和电脑同一个路由)连接
#启动App
d.app_start("com.ahdi.qrindo.wallet")
sleep(2)
#点击Top up
d(text="Top Up").click()
sleep(2)

#点击Debit Card
d(text = "Debit Card").click()
sleep(2)

#输入框中输入“12”
d(resourceId="com.ahdi.qrindo.wallet:id/et_amount").send_keys("12")

