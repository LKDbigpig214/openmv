import sensor,image,time,math

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time=2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()

f_x = (2.8 / 3.984) * 160
f_y = (2.8 / 2.952) * 120

c_x = 160 * 0.5
c_y = 120 * 0.5

def degrees(radians):
    return (180 * radians) / math.pi
    
while(True):
    clock.tick()
    img = sensor.snapshot()
    for tag in img.find_apriltags(fx=f_x, fy=f_y, cx=c_x, cy=c_y):
        img.draw_rectangle(tag.rect(), color = (255, 0, 0))
        img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))
        print_args = (tag.x_translation(), tag.y_translation(), tag.z_translation(),
             degrees(tag.x_rotation()), degrees(tag.y_rotation()), degrees(tag.z_rotation()))
        print("Tx: %f, Ty: %f, Tz: %f, Rx: %f, Ry: %f, Rz: %f" % print_args)
    print(clock.fps())
