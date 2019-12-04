import spacy
import json
class PartsofSpeech:

	def __init__(self, *arg,**kwargs):
		self.pos = list()
		self.nlp = spacy.load("en_core_web_sm")

	def get_articles(self,text):
		doc = self.nlp(text)
		print("Articles:", [token.lemma_ for token in doc if token.pos_ == "DET"])

	def get_pos(self,text):
		doc = self.nlp(text)
		for token in doc:
			self.pos.append({token.orth_:token.pos_})
			print(" {:<8} : {:<5} : {:<7} : {}".format(token.orth_,token.pos_,token.dep_,token.head))
		print(" {:<8} : {:<5} : {:<7} : {}".format("token","POS","dep.","head"))
		print("------------------------------------")
		return json.dumps(self.pos)


# pos=PartsofSpeech()
# pos.get_pos("I drove home with an joy.")
