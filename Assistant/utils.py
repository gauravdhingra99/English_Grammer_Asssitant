import requests, json
from django.conf import settings 

class GetSuggestions:

	def __init__(self,*args,**kwargs):
		self.EP = "https://api.textgears.com/check.php"
		self.key = "9oDxfD7zSWPktd8q"

	def spellcheck(self,text):
	    QUERY=text
	    response = requests.get(self.EP,params={'text': QUERY,"key":self.key })
	    print(response.url)
	    print(response.text)
	    result=json.loads(response.text)
	    right_wrong_array=[]
	    if result["result"]:
	        for i in result["errors"]:
	            wrong=i['bad']
	            right=i['better']
	            right_wrong_dict={"wrong":wrong,"right":right}
	            right_wrong_array.append(right_wrong_dict)
	       
	    return right_wrong_array

# getsugg = GetSuggestions()
# print(getsugg.spellcheck("john is an boy"))







