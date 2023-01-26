import pyshorteners
long_url = input('enter long url :')
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
print('The shortened url is :',short_url)
