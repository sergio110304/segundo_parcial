import random, string

class Caracteres:
    def __init__(self, caracteres: str):
        self.caracteres = list(string.ascii_letters + string.digits + string.punctuation)

class Contraseña(Caracteres):
    def __init__(self, caracteres: str):
        super().__init__(caracteres)

    def contraseña(self):
        self.num = int(input('Ingrese cantidad de caracteres de la contraseña: '))
        random.shuffle(self.caracteres)
        self.contra=[]

        for i in range(self.num):
            self.contra.append(random.choice(self.caracteres))
        random.shuffle(self.contra)
        print("".join(self.contra))

nose = Contraseña("")
nose.contraseña()