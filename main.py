# Meet QuickBot: your friend

import nltk
import warnings
import subprocess  # For executing curl commands
import requests  # For fetching Google search results
from bs4 import BeautifulSoup  # For parsing HTML

warnings.filterwarnings("ignore")
nltk.download('punkt_tab')  # for downloading packages
#import tensorflow as tf
import numpy as np
import random
import string  # to process standard python strings

f = open('nlp-ans.txt', 'r', errors='ignore')
m = open('mod-py.txt', 'r', errors='ignore')
checkpoint = "./chatbot_weights.ckpt"
#session = tf.InteractiveSession()
#session.run(tf.global_variables_initializer())
#saver = tf.train.Saver()
#saver.restore(session, checkpoint)

raw = f.read()
rawone = m.read()
raw = raw.lower()  # converts to lowercase
rawone = rawone.lower()  # converts to lowercase
nltk.download('punkt')  # first-time use only
nltk.download('wordnet')  # first-time use only
sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)  # converts to list of words
sent_tokensone = nltk.sent_tokenize(rawone)  # converts to list of sentences 
word_tokensone = nltk.word_tokenize(rawone)  # converts to list of words

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

Introduce_Ans = ["My name is QuickBot.", "My name is QuickBot you can call me pi.", "I'm QuickBot :)", "My name is QuickBot, and my nickname is pi, and I am happy to solve your queries :)"]
GREETING_INPUTS = ("hello", "hi", "hiii", "hii", "hiiii", "hiiii", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "hii there", "hi there", "hello", "I am glad! You are talking to me"]
Basic_Q = ("what is python?", "what is python", "what is python?", "what is python.")
Basic_Ans = "Python is a high-level, interpreted, interactive and object-oriented scripting programming language. Python is designed to be highly readable. It uses English keywords frequently, whereas other languages use punctuation, and it has fewer syntactical constructions than other languages."

# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Checking for Basic_Q
def basic(sentence):
    for word in Basic_Q:
        if sentence.lower() == word:
            return Basic_Ans

# Checking for Introduce
def IntroduceMe(sentence):
    return random.choice(Introduce_Ans)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Generating response
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo_response = robo_response + "Hey sorry mate, didn't get ya!!"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response

# Generating response for module-related queries
def responseone(user_response):
    robo_response = ''
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo_response = robo_response + "Hey sorry mate, didn't get ya!!"
        return robo_response
    else:
        robo_response = robo_response + sent_tokensone[idx]
        return robo_response
def chat(user_response):
    user_response = user_response.lower()
    keyword = " module "
    keywordone = " module"
    keywordsecond = "module "

    # Usage command
    if user_response == "usage":
        return "To use me, you can ask questions like:\n- 'hello'\n- 'what is python?'\n- 'curl: <website>'\n- 'google: <search_query>'\n- 'extract: <domain> <extension> <filename>'"

    # Google search functionality
    if user_response.startswith("google:"):
        search_query = user_response.split("google:", 1)[1].strip()
        url = f"https://www.google.com/search?q={search_query}"
        search_response = requests.get(url)
        soup = BeautifulSoup(search_response.text, 'html.parser')
        results = soup.find_all('h3')  # Fetching the titles of search results
        if results:
            return "Google Search Results:\n" + "\n".join(result.get_text() for result in results)
        else:
            return "No results found."

    # cURL functionality
    elif user_response.startswith("curl:"):
        curl_command = user_response.split("curl:", 1)[1].strip()
        try:
            result = subprocess.run(f"curl {curl_command} -o index.html", shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                return "Page has been successfully cloned as 'index.html'."
            else:
                return f"An error occurred while executing cURL: {result.stderr.strip()}"
        except Exception as e:
            return f"An error occurred while executing cURL: {str(e)}"

    # Google Dorking functionality
    elif user_response.startswith("extract:"):
        parts = user_response.split("extract:", 1)[1].strip().split()
        if len(parts) == 3:
            domain, extension, filename = parts
            url = f"https://www.google.com/search?q=site:{domain}+\"{extension}\"+\"{filename}\""
            search_response = requests.get(url)
            soup = BeautifulSoup(search_response.text, 'html.parser')
            results = soup.find_all('h3')  # Fetching the titles of search results
            if results:
                return "Dorking Results:\n" + "\n".join(result.get_text() for result in results)
            else:
                return "No results found."
        else:
            return "Please provide exactly three arguments: <domain> <extension> <filename>."

    if user_response != 'bye':
        if user_response == 'thanks' or user_response == 'thank you':
            return "You are welcome..Mate !!"
        else:
            if user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(keywordsecond) != -1:
                return responseone(user_response)
            elif greeting(user_response) is not None:
                return greeting(user_response)
            elif user_response.find("your name") != -1:
                return IntroduceMe(user_response)
            elif basic(user_response) is not None:
                return basic(user_response)
            else:
                return response(user_response)

    else:
        return "Bye Mate! take care.."
