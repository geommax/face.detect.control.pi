from time import sleep
import lcd_drivers
import RPi.GPIO as GPIO
import time
from time import sleep
from datetime import datetime
from subprocess import check_output


class AttendanceSystemControl:
    def __init__(self):
        self.lcd = lcd_drivers.Lcd()
        self.ip = check_output(["hostname", "-I"], encoding="utf8").split()[0]

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        self.servo1 = GPIO.PWM(11, 50)
        self.servo1.start(0)

    def long_string(self, text='', num_line=1, num_cols=16):
        if len(text) > num_cols:
            self.lcd.lcd_display_string(text[:num_cols], num_line)
            for i in range(len(text) - num_cols + 1):
                text_to_print = text[i:i + num_cols]
                self.lcd.lcd_display_string(text_to_print, num_line)
                sleep(0.2)
            sleep(0.5)
        else:
            self.lcd.lcd_display_string(text, num_line)

    def intro(self):
        self.lcd.lcd_display_string("System Starting!", 1)
        self.long_string("Welcome WYTU Attendance System", 2)
        sleep(0.5)
        self.lcd.lcd_clear()                                        
        self.lcd.lcd_backlight(0) 
        
    def sensorsTest(self):
        sleep(0.5)
        self.lcd.lcd_backlight(1)
        self.lcd.lcd_display_string("Testing Sensors.", 1)
        self.lcd.lcd_display_string(" Warming Servo! ", 2)
        ctl_system.moveServo()
        self.lcd.lcd_clear()
        self.lcd.lcd_display_string("Starting Camera!", 1)
        sleep(2)                                 
        self.lcd.lcd_backlight(0)
        self.lcd.lcd_clear()

    def allsensorsReadyAndCameraReady(self):
        sleep(0.5)
        self.lcd.lcd_backlight(1)
        self.lcd.lcd_display_string(" Camera Started ", 1) 

    def runningState(self): # For Ko Min Khaung
        self.lcd.lcd_clear()
        self.lcd.lcd_display_string("     READY !    ", 1)
        self.long_string(datetime.now().strftime("  %b %d, %H:%M"), 2)
        

    def dataWriteLCD(self, studentName): # For Ko Min Khaung 
        self.lcd.lcd_clear()
        self.long_string(str(studentName), 1)
        self.long_string(datetime.now().strftime("  %b %d, %H:%M"), 2)
        sleep(1.7)

    def moveServo(self):
        # Move the servo from 0 to 72 degrees (duty 2 to 6)
        duty = 2
        self.long_string(" Opening Door ! ", 1)
        while duty <= 6:
            self.servo1.ChangeDutyCycle(duty)
            time.sleep(0.1)
            self.servo1.ChangeDutyCycle(0) 
            time.sleep(0.2)
            duty += 1
        
        # Pause for 2 seconds
        time.sleep(2)

        # Move the servo back to 0 degrees
        self.long_string(" Closing Door ! ", 1)
        while duty >= 2:
            self.servo1.ChangeDutyCycle(duty)
            time.sleep(0.1)
            self.servo1.ChangeDutyCycle(0)
            time.sleep(0.2)
            duty -= 1

    def cleanup(self):
        # Stop the servo and clean up GPIO
        self.servo1.stop()
        GPIO.cleanup()
        print("Servo stopped and GPIO cleaned up")

ctl_system = AttendanceSystemControl()
ctl_system.intro()
ctl_system.sensorsTest()
ctl_system.allsensorsReadyAndCameraReady()
#ctl_system.runningState() # For Ko Min Khaung 
#ctl_system.dataWriteLCD("Kyaw Swar Tun",) # For Ko Min Khaung 
ctl_system.cleanup()




