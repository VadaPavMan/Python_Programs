import pyjokes, pyttsx3

engine = pyttsx3.init()
joke = pyjokes.get_joke('en')
print(joke), engine.say(joke)
engine.runAndWait()

