'''In a project I need to convert multiple words separated by \n into multiple words separated by ,'''
text = input('input:')

while True: 
    
    word = input('input:')
    text = text + " , " + word
    print(text)