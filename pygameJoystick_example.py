import pygame

pygame.init()
pygame.joystick.init()
count= pygame.joystick.get_count()
print "Joystick count:",count

if count>0:
    j=pygame.joystick.Joystick(0)
    j.init()
    print "Joystick name: ",j.get_name()
    n=j.get_numbuttons()
    while 1:
        pygame.event.pump()
        for i in range(n):
            if j.get_button(i):
                print "Joystick, pressed: ",i
else:
    print "No joystick, BYE!! \a \a"
    