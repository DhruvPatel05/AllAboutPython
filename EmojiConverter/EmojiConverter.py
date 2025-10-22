message = input(">")
messages = message.split(' ')
# print(messages)
emojis = {
    ":)" : "😊",
    ":(" :"😞"
}
output = ""
for word in messages:
    output += emojis.get(word, word) + " "
print(output)