class VendingMachine:
    def __init__(self):
        self.inventory = {
            'chips': 10,
            'candy': 20,
            'cookies': 15
        }
        self.prices = {
            'chips': 1.50,
            'candy': 1.25,
            'cookies': 2.00
        }
        self.coins = {
            'quarters': 0.25,
            'dimes': 0.10,
            'nickels': 0.05,
            'pennies': 0.01
        }
        self.total_money = 0.0

    def display_menu(self):
        print("Welcome to the Snack Vending Machine!")
        print("Available snacks: chips, candy, cookies")
    
    def report(self):
        print("\nCurrent Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item.capitalize()}: {quantity}")
        print(f"Money: ${self.total_money:.2f}\n")
    
    def check_inventory(self, item):
        if item in self.inventory and self.inventory[item] > 0:
            return True
        else:
            print(f"Sorry, {item.capitalize()} is out of stock.")
            return False
    
    def process_coins(self):
        total = 0.0
        print("Please insert coins (quarters, dimes, nickels, pennies):")
        for coin, value in self.coins.items():
            while True:
                try:
                    num_coins = int(input(f"Number of {coin}: "))
                    if num_coins < 0:
                        print("Please enter a valid number of coins.")
                        continue
                    total += num_coins * value
                    break
                except ValueError:
                    print("Invalid input! Please enter a number.")
        return total
    
    def calculate_change(self, change):
        change_breakdown = {}
        change = round(change, 2)  # Round the change to 2 decimal places
        for coin, value in sorted(self.coins.items(), key=lambda x: x[1], reverse=True):
            num_coins = int(change // value)
            if num_coins > 0:
                change_breakdown[coin] = num_coins
            change = round(change % value, 2)  # Update change after giving the coins
        return change_breakdown
    
    def transaction(self, item, payment):
        if payment < self.prices[item]:
            print("Insufficient funds. Money refunded.")
            return False
        elif payment > self.prices[item]:
            change = payment - self.prices[item]
            print(f"Here's ${change:.2f} in change.")
            change_breakdown = self.calculate_change(change)
            for coin, count in change_breakdown.items():
                print(f"{count} {coin}(s)")
            self.total_money += self.prices[item]
        else:
            self.total_money += self.prices[item]
        
        self.inventory[item] -= 1
        print(f"Here is your {item}. Enjoy!")
        return True
    
    def run_machine(self):
        while True:
            self.display_menu()
            choice = input("What snack would you like? (chips/candy/cookies): ").lower()
            
            if choice == 'off':
                print("Turning off the vending machine.")
                break
            elif choice == 'report':
                self.report()
            elif choice in ['chips', 'candy', 'cookies']:
                if self.check_inventory(choice):
                    payment = self.process_coins()
                    if self.transaction(choice, payment):
                        continue
            else:
                print("Invalid choice. Please try again.")
                continue

# Running the vending machine
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run_machine()
