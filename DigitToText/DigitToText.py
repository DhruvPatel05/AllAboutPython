phoneNumber = input("Enter the phone number: ")
strNumbers = ""
digit = ""
# for letter in phoneNumber:
#     if letter == '0':
#         digit = 'Zero'
#     elif letter == '1':
#         digit = 'One'
#     elif letter == '2':
#         digit = 'Two'
#     elif letter == '3':
#         digit = 'Three'
#     elif letter == '4':
#         digit = 'Four'
#     elif letter == '5':
#         digit = 'Five'
#     elif letter == '6':
#         digit = 'Six'
#     elif letter == '7':
#         digit = 'Seven'
#     elif letter == '8':
#         digit = 'Eight'
#     else:
#         digit = 'Nine'
#     strNumbers = f"{strNumbers} " +  digit
# print(strNumbers)
digits_mapping = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "0":"Zero"
}
for letter in phoneNumber:
    strNumbers += digits_mapping.get(letter, "!") + " "
print(strNumbers)