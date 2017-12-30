# -- coding: utf-8 --

def Associations(word):
 import urllib2
 import json
 #word=u'значение'
 #talkBlocking(word)
 word1=word.split()[0].decode('utf-8')
 print word1
 word_utf8=word1.encode('utf-8')
  
 value_url = urllib2.quote(word_utf8)
 url = "http://www.serelex.org/find/ru-skipgram-librusec/" + value_url
 print url
 req = urllib2.Request(url)
 
 opener=urllib2.build_opener()
 f = opener.open(req)
 json = json.loads(f.read())
 i01.ear.stopListening()
 for i in range(12):
	result=json['relations'][i]["word"]
	if word1.find(result[:-2])!=-1: pass
	else:
	 talkBlocking(unicode(result,"utf-8"))
	 #print unicode(result,"utf-8")
	 sleep(1)
 i01.ear.startListening()
