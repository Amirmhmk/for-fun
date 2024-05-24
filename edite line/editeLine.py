try:
    file = open("text.txt" , 'r')
    text = file.read()
    file.close()
except:
    print("error")

text = text.split('\n')
new_text = ""
for line in text:
    new_text = new_text + ' ' + line

try:
    file = open('NewText.txt' , 'w+')
    file.write(new_text)
    file.close()
except:
    print("error")