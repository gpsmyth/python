inputs = {"up": [1, -2],
          "down": [1, 2],
          "w": [0, -2],
          "s": [0, 2]}

#def keydown(key):
#    for i in inputs:
#        if key == simplegui.KEY_MAP[i]:
#            paddle_vel[inputs[i][0]] += inputs[i][1]

for i in inputs :
    print inputs[i][0], inputs[i][1]

def thrust_on() :
    print "You could invoke a class my_ship.thrust_on() method here"

def do_180() :
    print "You could invoke a class my_ship.do_180() method here"
    print "   self.angle += math.pi"
    print " self.vel[0] *= -1"
    print "    self.vel[1] *= -1"

def shoot() :
    print "The space bar would activate the shoot method"

# This dictionary declaration need to locatated after fn pointer method names
fns = {
    "up" : thrust_on,
    "down" : do_180,
    "space" : shoot }

for i in fns :
    # use an if condition to qualify
    # if key == simplegui.KEY_MAP[i]:
    fns[i]()
