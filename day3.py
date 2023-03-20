class Human:

    #built-in
    def __init__(self,name):
        self.name=name
        print("bir human instance ı uretildi")
    def __str__(self):
        return f"STR fonksiyonundan dönen değer: {self.name}"
    def talk(self,sentence):
        name="ayse"
        print(f"{self.name}:  {sentence}")
    def walk(self):
        print(f"{self.name}  is walking...")

#instance:

human1=Human("enes")

human1.talk("mrb!!!")
human1.walk()
print(human1)
