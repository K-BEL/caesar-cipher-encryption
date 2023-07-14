alphabet = "abcdefghijklmnopqrstuvwxyz"
text = str(input('enter your text:'))
k = int(input('tap the key :'))
newtext = " "
for i in text:
    if i in alphabet:

        position = alphabet.find(i)
        newposition = (position + k) % 26
        newi = alphabet[newposition]
        newtext += newi
    else:
        newtext = newtext + " "
print(newtext)
