import speech_recognition as sr # Reconhecimento de voz
import pyttsx3 # Respostas (Maquina)
import openai

openai.api_key = "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"

def generate_prompt(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message.strip()

audio = sr.Recognizer()
may = pyttsx3.init()

def runCommand():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            user = audio.listen(source)
            command = audio.recognize_google(user, language='pt-BR')
            command = command.lower()
            if 'may' in command:
                command = command.replace('may', '')
                may.say(command)
                may.runAndWait()
    except:
        print('O microfone não está conectado.')

    return command

prompt = runCommand()

may.say(generate_prompt(prompt))
may.runAndWait()
print(generate_prompt(prompt))