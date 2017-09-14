import time
from gpiozero import MotionSensor
# from gpiozero import LED

pir = MotionSensor (4)
# redled = LED(26)
# greenled = LED(19)

while True:
    pir.wait_for_motion()
    # redled.off()
    # greenled.on()
    # greenled.blink(1)
    print("Motion Detected")
    command = 'publish.py -e acy7b2a1mw1po.iot.eu-west-2.amazonaws.com -r root-CA.crt -c motionpi-00.cert.pem -k motionpi-00.private.key'
    os.system(command)
    time.sleep(5)
    # greenled.off()
    # redled.on()
    # redled.blink(1)
