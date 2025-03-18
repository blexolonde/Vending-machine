### Vending Machine Program

This Python program simulates the operation of a simple snack vending machine. It allows users to choose from three snack items, insert coins, and receive their selected item along with any change if they overpay. The machine tracks the inventory, handles payments, and displays a report of the total money collected and the available stock.

---

### Features:
1. **Snack Selection**: Users can choose from three snacks:
   - Chips ($1.50)
   - Candy ($1.25)
   - Cookies ($2.00)

2. **Coin Insertion**: Users insert coins (quarters, dimes, nickels, pennies) to pay for the selected snack. The program calculates the total amount inserted.

3. **Transaction Processing**:
   - If the user inserts enough money, the snack is dispensed.
   - If the user overpays, the program calculates and gives back the correct change, broken down into coins.
   - If the user underpays, the program alerts them that the funds are insufficient and refunds the money.

4. **Inventory Management**: The program checks if the selected snack is in stock. If the item is out of stock, the user is informed.

5. **Reporting**: Users can request a report that shows the current inventory of snacks and the total money collected by the machine.

6. **Shutdown**: The machine can be turned off by typing "off".

---

### Usage:
1. **Start the machine**: The machine will display a menu with available snacks.
2. **Select a snack**: Type the name of the snack you want (chips, candy, or cookies).
3. **Insert coins**: Enter the number of each type of coin (quarters, dimes, nickels, pennies) you want to insert.
4. **Get your snack**: If the payment is valid, the snack will be dispensed. If the payment is insufficient, the money will be refunded.
5. **Turn off the machine**: Type "off" to stop the machine.

### Example:
```
Welcome to the Snack Vending Machine!
Available snacks: chips, candy, cookies
What snack would you like? (chips/candy/cookies): candy
Please insert coins (quarters, dimes, nickels, pennies):
Number of quarters: 20
Number of dimes: 10
Number of nickels: 10
Number of pennies: 10
Here's $5.35 in change.
21 quarter(s)
1 dime(s)
Here is your candy. Enjoy!
```

---

### Requirements:
- Python 3.x

This is a simple command-line program that simulates a vending machine experience!
