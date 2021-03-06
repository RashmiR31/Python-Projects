# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:07:41 2020

@author:Rashmi R
"""


from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

##Speech to Text##

url_s2t = "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/82d9140a-e518-4fe9-928d-1f73e3c6608d"
iam_apikey_s2t = "lQrzjw62_5PjhzXM5f7SkulOIyBN9Ikxua6rV_Isbqh1"


authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t

filename='PolynomialRegressionandPipelines.mp3'
with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
response.result
from pandas.io.json import json_normalize

json_normalize(response.result['results'],"alternatives")
recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
print(recognized_text)

##Language Translator##

from ibm_watson import LanguageTranslatorV3

url_lt='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/778e01e6-3ca6-4d24-9432-7dbc16344786'
apikey_lt='Spg3lPo7lNCpvfo80rUDrpUhJ592_FLpofo3l7h3ddOO'


version_lt='2018-05-01'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)

from pandas.io.json import json_normalize

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")
translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
translation=translation_response.get_result()
spanish_translation =translation['translations'][0]['translation']

print('spanish:',spanish_translation)


translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()
translation_eng=translation_new['translations'][0]['translation']

print('English:',translation_eng)

French_translation=language_translator.translate(
    text=translation_eng , model_id='en-fr').get_result()
print('French:',French_translation['translations'][0]['translation'])
