# Garett Brown
import random

def plinko_run(x):
  for i in range(12):
    if x == 1: direction = 0.5
    elif x == 9: direction = -0.5
    else: direction = random.choice([-0.5, 0.5])
    x += direction
  return int(x - 1)
  
def user_input(prompt):
  output = -1
  while output == -1:
    user_number = input(prompt)
    try:
      output = int(user_number)
      if output > 0 and output < 10:
        return output
      else:
        output = -1
    except:
      output = -1
    print('Choose an integer between 1 and 9 inclusive.')
      
chips = user_input('How many chips do you have?')
prize_money = [1, 5, 10, 0, 50, 0, 10, 5, 1]
winnings = 0
number_of_games = 0
while chips > 0:
  number_of_games += 1
  chips -= 1
  position = user_input('Choose a slot to drop the chip down?')
  position = plinko_run(position)
  winnings += prize_money[position]
  if position == 0 or position == 8:
    chips += 1
    print('You won $' + str(prize_money[position]) + ' and another chip.\n')
  else:
    print('You won $' + str(prize_money[position]) + '.\n')

print('Total winnings: $' + str(winnings) + ' with ' + str(number_of_games) + ' chips.')
