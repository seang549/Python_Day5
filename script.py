# fruits= ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)

# # Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
  
# # Write your code below this row 👇
# count = 0
# current_height = 0
# for height in student_heights:
#   current_height += height
#   count += 1
# print(f"total height = {current_height}")
# print(f"number of students = {count}")
# print(f"average height = {format(current_height/count, '.0f')}")

# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# # Write your code below this row 👇

# current_score = 0
# for score in student_scores:
#   if current_score > score:
#     current_score = current_score
#   else:
#     current_score = score
# print(f"The highest score in the class is: {current_score}")

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# target = int(input()) # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️

# # Write your code here 👇

# total = 0
# for number in range(0, target + 1, 2):
#   total += number
# print(total)

# Write your code here 👇

for number in range(1, 101):
  if number % 15 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)