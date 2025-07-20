import pyjokes, pyttsx3

engine = pyttsx3.init()
joke = pyjokes.get_joke('en')
print(joke), engine.say(joke)
engine.save_to_file(joke, 'tTos.mov')
engine.runAndWait()
