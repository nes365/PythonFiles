import pickle , urllib.request
 
url = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
 
picture = pickle.load(url)
 
for line in picture:
    print(''.join(c * n for c, n in line))
 


