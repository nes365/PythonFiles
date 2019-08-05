import urllib
def gotonextpage():
	urltoget = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+nextnum
nextnum = "12345"
for i in range(0,400):
	getnewnum = []
	#follow url path by inputting next number into website chain
	urltoget = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+nextnum
	content_of_url = urllib.urlopen(urltoget).read()
	for i in range(0, len(content_of_url)):
		if content_of_url[i].isdigit():
			getnewnum.append(content_of_url[i])
	print content_of_url
	nextnum = "".join(getnewnum)
	gotonextpage
