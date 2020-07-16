
class CoffeeMachine(object):


    def __init__(self, water, milk, beans, cups, money):
        self.cappuccino = [200, 100, 12, 6]
        self.latte = [350, 75, 20, 7]
        self.espresso = [250, 0, 16, 4]
        self.run = True
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def checking(self, choice):
        self.out_of = ''
        self.check = False
        if self.water - choice[0] < 0:
            self.out_of = 'water'
        elif self.milk - choice[1] < 0:
            self.out_of = 'milk'
        elif self.beans - choice[2] < 0:
            self.out_of = 'beans'
        elif self.cups == 0:
            self.out_of = 'cups'

        if self.out_of != '':
            print("Sorry, not enough" + self.out_of + "!")
        else:
            print('I have enough resources, making you a coffee!')
            self.check = True

    def making_coffee(self, choice):
        self.water -= choice[0]
        self.milk -= choice[1]
        self.beans -= choice[2]
        self.money += choice[3]
        self.cups -= 1

    def buy(self):
        print('Select the type of coffee:')
        print(' 1. Espresso')
        print(' 2. Latte')
        print(' 3. Cappuccino')
        print(' Back to main menu')
        coffee_type = input().strip()

        if coffee_type == '1':
            self.checking(self.espresso)
            if self.check:
                self.making_coffee(self.espresso)
        elif coffee_type == '2':
            self.checking(self.latte)
            if self.check:
                self.making_coffee(self.latte)
        elif coffee_type == '3':
            self.checking(self.cappuccino)
            if self.check:
                self.making_coffee(self.cappuccino)

        elif coffee_type == 'back':
            pass

    def fill(self):
        self.add_water = int(input("Write how many ml of water do you want to add: \n>"))
        self.add_milk = int(input("Write how many ml of milk do you want to add: \n>"))
        self.add_beans = int(input("Write how many grams of coffee beans do you want to add: \n>"))
        self.add_cups = int(input("Write how many disposable cups do you want to add: \n>"))

        self.water += self.add_water
        self.milk += self.add_milk
        self.beans += self.add_beans
        self.cups += self.add_cups

    def take(self):
        print("I gave you $", self.money)
        self.money = 0

    def remaining(self):
        print("The coffee machine has:")
        print(self.water, " ml of water")
        print(self.milk, " ml of milk")
        print(self.beans, " g of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, " of money")

    def options_menu(self):
        print("Write action: >buy  >fill  >take  >remaining  >exit:")
        self.option = input().strip().lower()
        if self.option =='buy':
            self.buy()
        elif self.option == 'fill':
            self.fill()
        elif self.option == 'take':
            self.take()
        elif self.option == 'remaining':
            self.remaining()
        elif self.option == 'exit':
            self.run = False



# total_water = 400
# total_milk = 540
# total_beans = 120
# total_cups = 9
# total_money = 550

cafeteira = CoffeeMachine(400, 540, 120, 9, 550)

while cafeteira.run:
    cafeteira.options_menu()
