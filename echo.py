import time

counter = 0
for i in range(0, 30):
    time.sleep(1)
    print "echo {}".format(counter)
    counter = counter + 1