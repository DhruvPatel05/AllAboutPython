# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')
# numbers = [5,2,5,2,2]
numbers = [1,1,1,1,1,1,1,10]
# for number in numbers:
#     # print(number)
#     print('x'* number)
for number in numbers:
    # print(number)
    strNum = ""
    for x in range(number):
      strNum += 'x'
    print(strNum)


