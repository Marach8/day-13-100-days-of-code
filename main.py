test_name = input('Enter the name of the test: ')
print()
maximum_score = int (input('Enter the maximum score of the test: '))
print()
score = float(input('Enter the score obtained: '))
print()
print(f'Performance of students in {test_name}')
print()
a = round(((score*100)/maximum_score),2)
if 90 <= a <= 100:
  print(f'\033[32mWo! You scored {a}%. That is an A+🎉\033[0m')
elif 80 <= a < 90:
  print(f'\033[032mYou scored {a}%. That is an A. Kudos👌\033[0m')
elif 70 <= a < 80:
  print(f'You scored {a}%. That is a B')
elif 60 <= a < 70:
  print(f'\033[33mYour score is {a}%. You got a C.\033[0m')
elif 50 <= a < 60:
  print(f'\033[33mYour score is {a}%. You got a D😥\033[0m')
elif a < 50:
  print(f'\033[31m You scored {a}%. You got an F😭\033[0m')
else:
  print('invalid score!')