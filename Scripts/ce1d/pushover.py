#! /usr/bin/python
import sys
import os
import random
import httplib, urllib
import urllib2
from datetime import datetime
conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json", 
urllib.urlencode({ 
"token": "a98hhVBULCrTmjKQ2hAgbx4V4z4hSe", 
"user": "ubYLUfY1QTXwKVBLoNikXKgYTfqdZe", 
"message": "Alarms would ring. %s" % str(sys.argv[1]),
}), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
urllib2.urlopen(ip).read()
