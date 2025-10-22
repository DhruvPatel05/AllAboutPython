message = input(">")
# messages = message.split(' ')
# # print(messages)
# emojis = {
#     ":)" : "😊",
#     ":(" :"😞"
# }
# output = ""
# for word in messages:
#     output += emojis.get(word, word) + " "
# print(output)
def emojiconverter(strmessage):
    messages = strmessage.split(' ')
    # print(messages)
    emojis = {
        ":)": "😊",
        ":(": "😞"
    }
    output = ""
    for word in messages:
        output += emojis.get(word, word) + " "
    return output


print(emojiconverter(message))
