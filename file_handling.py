import os

filename = input('Enter the file name: ')

if os.path.isfile(filename):
    f = open(filename, mode='w')
    f.writelines('Hello \n My name is Nevin \n My age is 6\n Im studying in Alnoor')
    lines = f.readlines()
    print('Total number of lines in the file: ',len(lines))
    word = char_count = 0
    list1 = []
    for content in lines:
        char_count += len(content) - 1
        for i in content:
            if ' ' in i:
                word += 1
                char_count -= 1
        word += 1
    print('Total word count: ', word)
    print('Total char count: ', char_count)
    f.close()

else:
    print('File is not present')