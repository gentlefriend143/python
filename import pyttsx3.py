import pyttsx3

assistant = pyttsx3.init('sapi')
voices= assistant.getproperty('voices')
print(voices)
assistant.setproperty('voices',voices[0].id)
