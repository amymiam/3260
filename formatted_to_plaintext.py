# used for comparing plaintext to formatted plaintext to ensure the formatting did not introduce errors

with open(input("formatted text file: "), "r") as ft:
    formatted_text = ft.read()

with open(input("plaintext file: "), "r") as pt:
    plaintext = pt.read()

formatted_text = "".join([char for char in formatted_text.lower() if char.isalpha()])
plaintext = "".join([char for char in plaintext.lower() if char.isalpha()])

# basic statistics + where the first difference is, if there is one

print(formatted_text)
print(len(formatted_text))
print(plaintext)
print(len(plaintext))
print(formatted_text == plaintext)
for i in range(min(len(formatted_text), len(plaintext))):
    if formatted_text[i] != plaintext[i]:
        print(formatted_text[i-10:i+1])
        break