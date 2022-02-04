from translate import Translator


translator = Translator(to_lang='japanese')

try:
	with open('test1.py.txt', mode='r') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		print(translation)
	with open('new_file.txt',mode='a',encoding="utf-8") as out_file:
		out_file.write(translation)
except FileNotFoundError as err:
    print('File does not exist')
except IOError as err:
    print('I/O error')
