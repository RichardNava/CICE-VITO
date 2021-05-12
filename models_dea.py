
class Dea():

    def __init__(self, dea_code, pos_x, pos_y):
        self.dea_code = dea_code
        self.pos_x = pos_x
        self.pos_y = pos_y

    def calculate_distance(self, user_x, user_y):
        result = ((user_x - self.pos_x)**2 + (user_y - self.pos_y)**2)**0.5
        return result

class User():
    
    def __init__(self, name, password):
        self.name = name
        self.password = password
