class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

    def change_name(self, new_name):
        self.name = new_name
        return self.name
    
    def change_age(self, new_age):
        self.age = new_age
        return self.age
    
    def add_track(self, new_track):
        self.track = self.track.append(new_track)
        return self.track
    
    def get_score(self):
        return self.score


            
Bob = Student(name= "Bob", age = 26, track = ["FE","BE"], score = 20.90)

# Expected methods
Bob.change_name("Peter")
print(Bob.name)

Bob.change_age(34)
print(Bob.age)

Bob.add_track("UI/UX")
print(Bob.track)

Bob.get_score()
print(Bob.get_score())
