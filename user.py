class User:
    def __init__(self, first_name, last_name, email_address, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email_address
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First name: {self.first_name}\nLast name: {self.last_name}\nEmail: {self.email}\nAge: {self.age}")
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else: 
            print(f"{self.first_name} is already a member.")
        return self

    def spend_points(self, amount):
        if self.gold_card_points - amount < 0:
            print(f"{self.first_name} does not have sufficient points.")
        else:
            self.gold_card_points -= amount
        return self

taemin = User("Taemin", "Lee", "leetaemin@smentertainment.com", 29)
jonghyun = User("Jonghyun", "Kim", "kimjonghyun@smentertainment.com", 27)
key = User("Kibum", "Kim", "kimkibum@smentertainment.com", 31)
taemin.display_info()
taemin.enroll()
taemin.spend_points(50)
jonghyun.enroll()
jonghyun.spend_points(150)
taemin.display_info()
jonghyun.display_info()
key.display_info()
jonghyun.spend_points(100)
taemin.enroll()