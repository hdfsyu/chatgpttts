import pyttsx3
import openai
engine = pyttsx3.init()
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 100)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
openai.api_key = "sk-xxxx"
model="gpt-3.5-turbo"
while True:
    engine.say("Hi! I am ChatGPT, model " + model + ", what do you want to ask me?")
    engine.runAndWait()
    message_input = input("Hi! I am ChatGPT, model " + model + ", what do you want to ask me? ")
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": message_input},
            ]
    )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    engine.say(result)
    engine.runAndWait()
    print(result)