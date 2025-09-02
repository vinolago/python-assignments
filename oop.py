#Assignment 1: Player Scouting System: 
# The Scouting department submit player evaluations.
#The Recruitment department check those reports and decide whether to proceed with buying.

#Uses inheritance and polymorphism to unify evaluation handling.

class Player:
    def __init__(self, name:str, age: int):
        self._name = name
        self._age = age
    
    def evaluate(self):
        raise NotImplementedError("All departments must implement evaluate()")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
    
class Scouting(Player):
    def __init__(self, name, age, player_position: str):
        super().__init__(name, age)
        self.player_position = player_position
        self.player_report= []

    def evaluate(self):
        return f"{self.name} is a the best young player in his position: {self.player_position}."

    def scouting_report(self, report: str):
        self.player_report.append(report)
        return f"Report added: {report}"
    
class Recruitment(Player):
    def __init__(self, name: str, age: int, club: str, transfer_fee: int, player_salary: int):
        super().__init__(name, age )
        self.club = club
        self.transfer_fee = transfer_fee
        self.player_salary = player_salary

    def evaluate(self):
        return f"{self.name} is valued at ${self.transfer_fee} by club {self.club}"

    def buy_player(self, scouting: Scouting, approved):
        print(f"Send ${self.transfer_fee} offer for player {self.name} based on scouting: {scouting.evaluate()}. Approved: {approved}")
        scouting.scouting_report(f"Approved: {approved}")

lead_scout= Scouting("Leny Yoro", 18, 'DEF')
head_of_recruitment = Recruitment("Leny Yoro", 18, "Lille", 52000000, 120000 )

print(lead_scout.evaluate())
print(head_of_recruitment.evaluate())
head_of_recruitment.buy_player(lead_scout, approved=True)


#Assigment 2: Polymorphism Challenge
#How do I travel to see you?

class Air:
    def move(self):
        return f"The plane might crash!"
    
class Road:
    def move(self):
        return f"The car might crash!"
    
class Sea:
    def move(self):
        return f"The boat might sink!"
    
class Train:
    def move(self):
        return f"Train does not reach the destination!"
    
class Walk:
    def move(self):
        return f"I have no option but to walk."
    
def travel_method(travel):
    print(travel.move())

air = Air()
road = Road()
sea = Sea ()
train = Train()
walk = Walk()

travel_method(air)
travel_method(road)
travel_method(sea)
travel_method(train)
travel_method(walk)


