#permite que un metodo pueda cambiar de contexto o entorno y seguir cumpliendo su función adaptandose
# a lo nuevos cambios

class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Wof"
    
def sound2(animal):
        print(animal.sound())
        
plomito = Cat()
Lola = Dog()

sound2(plomito)