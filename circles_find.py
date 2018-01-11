import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
clock = time.clock()

while(True):
    clock.tick()
    
    img = sensor.snapshot().lens_corr(1.8)
    
    for c in img.find_circles(threshold = 2000, x_margin = 10, y_margin = 10, r_margin = 10):
        img.draw_circle(c.x(), c.y(), c.r(), color = (255, 0, 0))
        print(c)
    print("FPS %f" % clock.fps())
