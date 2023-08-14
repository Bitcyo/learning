#LSP, Los objetos de la clase dnerian ser modifocables en las sub clases de este sin 
#afectar el funcionamiento de la clase base


#class Bird:
#    def fly(self):
#        print("fying...")

#class Penguin(Bird):
#    def fly(self):
#        return 'not can flying'
#def do_flying(bird = Bird):
#    return bird.fly()

#print(do_flying(Penguin()))


class Bird:
    pass

class BirdFly(Bird):
    def flying(self):
        return "no flying"

class BirdNoFly():
    pass