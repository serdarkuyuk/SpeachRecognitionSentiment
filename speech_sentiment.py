import speech_recognition as sr
from textblob import TextBlob
import re
from yelpapi import YelpAPI
import yelp_crediatials

def clean_text(text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

def analyze_sentiment(text):
    analysis = TextBlob(text)
    
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

def search_yelp():

    client_id = yelp_crediatials.client_id
    api_key = yelp_crediatials.api_key


    yelp_api = YelpAPI(api_key)
    term = 'Mexican restaurant bar'
    location = 'Boston, MA'
    search_limit = 50
    response = yelp_api.search_query(term = term,
                                     location = location,
                                     limit = search_limit)
    print(response)
    
    '''
    cols = list(response['businesses'][0].keys())
    data = pd.DataFrame(columns=cols)
    for biz in response['businesses']:
        data = data.append(biz, ignore_index=True)
    data.head()
    '''

def listen_mic():
    print("startting")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text = clean_text(text)
            sentiment = analyze_sentiment(text)
            print("You said : {},{}".format(text, sentiment))
        except:
            print("Sorry could not recognize what you said")
        return text

def main():
    #search_yelp()
    listen_mic()



if __name__ == '__main__':
    main()





