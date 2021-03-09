import wolframalpha
client = wolframalpha.Client("AA2VH3-PA98T59LH5")

import PySimpleGUI as sg

import wikipedia

import pyttsx3
engine = pyttsx3.init()

sg.theme('DarkAmber')
layout = [  
            [sg.Text('Enter a command'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
         ]
window = sg.Window('Py AI', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences = 2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Results: "+wolfram_res,"Wikipedia Result: "+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

    #print(values[0])

window.close()