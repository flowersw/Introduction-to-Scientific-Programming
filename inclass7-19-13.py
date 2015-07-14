#!/usr/bin/env python

#Inclass 7-19-13
"""
import requests
r = requests.get('http://www.unc.edu')
string = r.text.encode('ascii', 'ignore')
# do analysis
print string
print string.count('the')
"""

#import requests
#r = requests.get("http://www.unc.edu")
#r.text.encode('ascii', 'ignore')
#from HTMLParser import HTMLParser
#
#class myParser(HTMLParser):
#    def handle_data(self, data ):
#        print data
#    def handle_starttag(self, tag, attr):
#        print tag, attr
#    def handle_endtag(self, tag):
#        print tag
#    
#    
#
##instantiate the parser and fed it some HTML
#obj = myParser()
#obj.feed('<html><body>this is test</body></html')
#
#
#
#import webapp2
#from paste import httpserver
#class HelloWorld(webapp2.RequestHandler):
#    def get(self):
#        self.response.write('Hello World!')
#app = webapp2.WSGIApplication([('/', HelloWorld),], debug=True)
#httpserver.serve(app, host='127.0.0.1', port='80

#dna sequence
from Bio.Seq import Seq
s = Seq("AGTACACTGGT")
print s
print s.complement()
print s.reverse_complement()
print s.count('A')

