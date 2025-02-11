def process_text_file(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    words = text.split('\n')
    print(words)


    with open(output_file, 'w') as file:
        for i in range (0 , len(words)):
            if i%50 == 0 :
                file.write(words[i] + '\n\n\n')
            else:
                file.write(words[i] + ' , ' )



def process_text_file2(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    words = text.split('\n')

    with open(output_file, 'w') as file:
        for i in range (0 , len(words)):
            parts = words[i].split(":")
            file.write(parts[0] + '\n' )


input_file = 'input.txt'
output_file = 'output.txt'

process_text_file(input_file, output_file)
