from transformers import pipeline
from textblob import TextBlob
from wandb import summary


'''text = "I don't love this product! It's not amazing."
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(f"Sentiment polarity: {sentiment}")
print(blob.sentiment)

classifier = pipeline('sentiment-analysis')
result = classifier(text)
print(result)
'''

generator = pipeline("text-generation")

print(generator("Write an email to sell a domain name: oaklandremodel.com", max_length=20))


'''text_to_audio = pipeline("text-to-audio")
text = """The COVID-19 pandemic has had a profound impact on global health, economies, and daily life. It has led to widespread illness and loss of life, as well as significant disruptions to businesses and education. Governments around the world have implemented various measures to control the spread of the virus, including lockdowns, social distancing, and vaccination campaigns. The pandemic has also highlighted the importance of public health infrastructure and the need for global cooperation in addressing health crises. As the world continues to navigate the challenges posed by COVID-19, it is crucial to learn from this experience and strengthen our preparedness for future pandemics."""
audio = text_to_audio(text)
print(audio)'''
