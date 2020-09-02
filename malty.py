import webbrowser, sys, pyperclip, requests

'''Step one'''

# print(webbrowser.open('http://inventwithpython.com/'))   # This help to open the url to a specified page

# print(webbrowser.open("http://maps.google.com/"))
# print(webbrowser.open("https://www.google.com/maps/place/870+ Valencia+St+San+Francisco+CA/"))

'''Step two'''


'''Knowing about the sys.argv' : it is use to pass the command line argument in to our script'''
# print("This is the name of the script: ", sys.argv[0])
# print("This is the name of the script: ", sys.argv[1])
# print("Number of arguments: ", len(sys.argv))
# print("The arguments are: " , str(sys.argv))

# if len(sys.argv) > 1 :
# 	# address = sys.argv
# 	address = " ".join(sys.argv[1:])
# else:
# 	address = pyperclip.paste()

# webbrowser.open('https://www.google.com/maps/place/' + address)
	

# print(address)

""" USING REQUESTS TO DOWNLOAD A WEBPAGE USING requests.get() """

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt') 
# print(type(res))
print(len(res.text))
copy = pyperclip.copy(res.text)   # to copy the page in string format to my clipboard
# print(res.text)

try:
	res.raise_for_status()  # this method help to halt the download if there's a bad netword
except Exception as exc:
	print(f"There was a error : {exc}")
else:
	print("download successful")

# Saving the text that we copy to the clipboard to be paste to the our file using file I/O
text_paste = pyperclip.paste()
with open("Romeo and juliet.txt", mode = "wb")  as webscrape:
	for chunk in res.iter_content(100000):  # The ite_content() is used to iterate over the text as it is in the webpage
		webscrape.write(chunk)











