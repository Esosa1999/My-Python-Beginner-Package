import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3


symbol_count= { 'A': 2, 'B': 4, 'C': 6, 'D': 8} 
symbol_values= { 'A': 5, 'B': 3, 'C': 2, 'D': 1} 


def check_winnings(columns, lines, bet, values): 
     winnings=0
     winnings_lines=[]
     for line in range(lines):
          symbol=columns[0][line]
          for column in columns:
               symbol_to_check=column[line]
               if symbol !=symbol_to_check:
                    break
          else:
             winnings+=values[symbol] * bet
             winnings_lines.append(line + 1)

     return winnings, winnings_lines


def get_slot_machine_spin(rows,cols,symbols):
     all_symbols=[]
     for symbol, symbol_count in symbols.items(): 
          for _ in range(symbol_count):
               all_symbols.append(symbol)


     columns=[]
     for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
          value=random.choice(current_symbols)
          current_symbols.remove(value)
          column.append(value)

        columns.append(column)
     
     return columns


def print_slot_machine(columns):
     for row in range(len(columns[0])):
          for i, column in enumerate(columns):
               if i!=len(columns) - 1:
                   print(column[row], end=' | ')
               else:
                    print(column[row], end='')
          print()


# Function to deposit
def deposit():
    while True:
         Amount= input('what would you like to deposit?  $')
         if Amount.isdigit():
              Amount=int(Amount)
              if Amount>0:
                   break
              else:
                   print('Amount must be greater than 0.')
         else:
              print('Please enter a number.')          
    return Amount

# function to choose the number of lines a user will be betting on
def get_number_of_lines():
     while True:
          lines=input('Enter the number of lines to bet on (1' + '-' + str(MAX_LINES) + ')? ')
          if lines.isdigit():
               lines=int(lines)
               if 1<=lines<=MAX_LINES:
                    break
               else:
                    print('Enter a valid number of lines')
          else: 
               print('Please enter a number.')
     return lines


# function for the amount of money the user will bet
def get_bet():
     while True:
          amount=input('What would you like to bet? $')
          if amount.isdigit():
               amount=int(amount)
               if MIN_BET<=amount<=MAX_BET:
                    break
               else:
                    print('Please input a value between',  MIN_BET, 'and', MAX_BET)
          else:
               print('Please enter a number')
     return amount               

def spin():
    balance=deposit()
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        Total_bet= bet * lines

        if Total_bet>balance:
             print(f'You do not have enough to bet that amount. Your current balance is ${balance}')
        else:
             break
    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${Total_bet}')


    slots= get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings,winnings_lines=check_winnings(slots,lines,bet,symbol_values)
    print(f'You won ${winnings}.')
    print(f'you won on lines:', *winnings_lines)
    return winnings - Total_bet

         

def main():
    balance=deposit()
    while True:
         print(f'Current balance is: ${balance}')
         answer= input('press enter to play (q to quit).')
         if answer=='q':
              break
         balance= balance+spin()

    print(f'You left with ${balance}')

main()

    