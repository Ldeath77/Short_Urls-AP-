import seolib as seo
import pickle
import re
import mechanize
from mechanize import Browser
br = Browser()
br.set_handle_robots( False )
br.addheaders = [('User-agent', 'Firefox')]
res=br.open("http://www.google.com/")
print res.code
print res.text
for f in br.forms():
    print f
