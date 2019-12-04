from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
import json
from Assistant.utils import GetSuggestions
from Assistant.pos import PartsofSpeech
class GrammerCheckView(View):
    Template_name = "index.html"

    def get(self, request):
        return render(self.request,self.Template_name)

    def post(self,request):
    	if self.request.is_ajax():
    		body_unicode = self.request.body.decode('utf-8')
    		parsed_data = json.loads(body_unicode)
    		query = parsed_data['query']
    		get_suggestions = GetSuggestions()
    		suggestions = get_suggestions.spellcheck(query)
    		return JsonResponse({"data":suggestions})
    	else:
    		query = self.request.POST.get('query',None)
    		if query:
    			print(query)
	    		get_suggestions = GetSuggestions()
    			suggestions = get_suggestions.spellcheck(query)
    			return render(self.request,self.Template_name,locals())


class PosView(View):
    Template_name = "index.html"

    def get(self, request):
        return render(self.request,self.Template_name)

    def post(self,request):
    	if self.request.is_ajax():
    		body_unicode = self.request.body.decode('utf-8')
    		parsed_data = json.loads(body_unicode)
    		query = parsed_data['query']
    		print('aaaaaaaaaaaaaaa',query)
    		getpos = PartsofSpeech()
    		pos = getpos.get_pos(query)
    		print(pos)
    		return JsonResponse({"data":pos})
    	# else:
    	# 	query = self.request.POST.get('query',None)
    	# 	if query:
    	# 		print(query)
	    # 		get_suggestions = GetSuggestions()
    	# 		suggestions = get_suggestions.spellcheck(query)
    	# 		print(suggestions)
    	# 		print(suggestions[0]['wrong'])
    	# 		return render(self.request,self.Template_name,locals())
