class MainCharacter:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def introduce_self(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I work as a {self.occupation}.")

main_character = MainCharacter("John Doe", 30, "Software Engineer")
main_character.introduce_self()