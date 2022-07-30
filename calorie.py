from temperature import Temperature

class Calorie:

    def __init__(self,weight, height, age, temperature, gender):
        self.gender = gender
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        gender = str(self.gender).capitalize()
        if gender == "Male":
            result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10 + 5
        else:
            result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10 - 161

        return result

