import requests
import json 

def spellcheck(text):
    textToCheck=text.replace(" ", "+")
    url = "https://api.textgears.com/check.php?text="+textToCheck+'&key=9oDxfD7zSWPktd8q'
    response=requests.request("POST", url)
    result=json.loads(response.text)
    right_wrong_array=[]
    if result["result"]:
        for i in result["errors"]:
            wrong=i['bad']
            right=i['better']
            right_wrong_dict={"wrong":wrong,"right":right}
            right_wrong_array.append(right_wrong_dict)
       
    return right_wrong_array
        # print(right_wrong_array)
        # for j in right_wrong_array:
            #Taking the first right suggestion 

            # k=0
            # if c==0:
            #     if(len(j['right'])>5):
            #         while(k<5):
            #             # print(j['wrong'],j['right'][k])
            #             # print(text)
            #             # text=text.replace(j['wrong'],j['right'][k])
            #             # print(j['wrong'],j['right'][k])
            #             sentence_suggestion_array.append(text.replace(j['wrong'],j['right'][k]))
            #             k=k+1
            #     else:
            #         while(k<len(j['right'])):
            #             text=text.replace(j['wrong'],j['right'][k])
            #             sentence_suggestion_array.append(text)
            #             k=k+1
            # else:
            #     if(len(j['right'])>5):
            #         l=(c*5)-5                       
            #         while(k<5):
            #             text=sentence_suggestion_array[l].replace(j['wrong'],j['right'][k])
            #             sentence_suggestion_array.append(text)
            #             k=k+1
            #         l=l+1
            #     else:
            #         l=(c*len(j['right']))-len(j['right'])                       
            #         while(k<len(j['right'])):
            #             text=sentence_suggestion_array[l].replace(j['wrong'],j['right'][k])
            #             sentence_suggestion_array.append(text)
            #             k=k+1
            #             l=l+1
            # c=c+1


        # right_wrong_array.append({"correct_sentence":text})
    
        # return sentence_suggestion_array


print(spellcheck("gaurav ik nst an goood boy"))





