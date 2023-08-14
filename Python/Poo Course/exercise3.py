#creando personajes que al fusionarse sus habilidades incrementen

class Characters:
    def __init__(self, force, speed, resistance):
        self.force = force
        self.speed = speed
        self.resistance = resistance
        
    def __repr__(self):
        return f'force: {self.force}, speed: {self.speed}, resistance: {self.resistance}'
        
    def __add__(self, other):
        new_force = ((self.force + other.force)/2)**2
        new_speed = ((self.speed + other.speed)/2)**2
        new_resistance = ((self.resistance + other.resistance)/2)**2
        
        return Characters(new_force, new_speed, new_resistance)
    

        
plomito = Characters(20, 60, 50)
canelo = Characters(39, 70, 20)

ploninelo = plomito + canelo

print(ploninelo)

