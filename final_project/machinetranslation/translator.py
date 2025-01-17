'''Operating system functionality to read the .env file'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Create an instance of the IBM Watson Language translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com'
)

# Function to translate English to French
def english_to_french(english_text):
    ''' Translate the english text input to french'''
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    return french_text

# Function to translate French to English
def french_to_english(french_text):
    ''' Translate the french text input to english'''
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    return english_text
