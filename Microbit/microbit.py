def showLED(key: str):
    if key == "LED_READY":
        robotbit.rgb().set_pixel_color(0, neopixel.colors(NeoPixelColors.YELLOW))
        robotbit.rgb().show()
    if key == "LED_PUB":
        robotbit.rgb().set_pixel_color(0, neopixel.colors(NeoPixelColors.GREEN))
        robotbit.rgb().show()
    if key == "LED_OFF":
        robotbit.rgb().set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
        robotbit.rgb().show()

def on_uart_data_received():
    global bleReceivedValue
    bleReceivedValue = bluetooth.uart_read_until(serial.delimiters(Delimiters.DOLLAR))
    serial.write_line(bleReceivedValue)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.DOLLAR), on_uart_data_received)

# Mecanum wheel lego robot

def on_data_received():
    global direction
    direction = serial.read_until(serial.delimiters(Delimiters.DOLLAR))
    executeMotion(direction, defaultValue)
serial.on_data_received(serial.delimiters(Delimiters.DOLLAR), on_data_received)

def on_bluetooth_connected():
    music.set_volume(255)
    music.ring_tone(988)
    basic.pause(100)
    music.set_volume(0)
    music.stop_all_sounds()
    robotbit.rgb().set_pixel_color(1, neopixel.colors(NeoPixelColors.BLUE))
    robotbit.rgb().show()
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    music.set_volume(255)
    music.ring_tone(262)
    basic.pause(100)
    music.set_volume(0)
    music.stop_all_sounds()
    robotbit.rgb().set_pixel_color(1, neopixel.colors(NeoPixelColors.BLACK))
    robotbit.rgb().show()
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def driveMotors(m1a: number, m1b: number, m2a: number, m2b: number):
    robotbit.motor_run(robotbit.Motors.M1A, m1a)
    robotbit.motor_run(robotbit.Motors.M1B, m1b)
    robotbit.motor_run(robotbit.Motors.M2A, m2a)
    robotbit.motor_run(robotbit.Motors.M2B, m2b)
def executeMotion(key2: str, value: number):
    if key2 == "N":
        driveMotors(0 - value, value, value, 0 - value)
    elif key2 == "S":
        driveMotors(value, 0 - value, 0 - value, value)
    elif key2 == "CW":
        driveMotors(0 - value / 4, 0 - value / 4, 0 - value / 4, 0 - value / 4)
    elif key2 == "CCW":
        driveMotors(value / 4, value / 4, value / 4, value / 4)
    elif key2 == "FCC":
        driveMotors(value / -3, value * 1, value * 1, value / -3)
    elif key2 == "FCW":
        driveMotors(value * -1, value / 3, value / 3, value * -1)
    elif key2 == "BCC":
        driveMotors(value * 1, value / -3, value / -3, value * 1)
    elif key2 == "BCW":
        driveMotors(value / 3, value * -1, value * -1, value / 3)
    elif key2 == "FL":
        driveMotors(value * 0, value * 1, value * 0, value * -1)
    elif key2 == "FR":
        driveMotors(value * -1, value * 0, value * 1, value * 0)
    elif key2 == "BL":
        driveMotors(value * 1, value * 0, value * -1, value * 0)
    elif key2 == "BR":
        driveMotors(value * 0, value * -1, value * 0, value * 1)
    elif key2 == "L":
        driveMotors(value, value, 0 - value, 0 - value)
    elif key2 == "R":
        driveMotors(0 - value, 0 - value, value, value)
    elif key2 == "STOP":
        robotbit.motor_stop_all()
    if key2 == "a01_on":
        robotbit.geek_servo(robotbit.Servos.S1, 15)
    if key2 == "a01_off":
        robotbit.geek_servo(robotbit.Servos.S1, 35)
    showLED(key2)
direction = ""
bleReceivedValue = ""
defaultValue = 0
bluetooth.start_uart_service()
serial.redirect(SerialPin.P14, SerialPin.P15, BaudRate.BAUD_RATE115200)
defaultValue = 255
robotbit.motor_stop_all()
showLED("led_off")
basic.show_icon(IconNames.HEART)