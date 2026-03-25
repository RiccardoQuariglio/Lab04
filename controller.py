import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def handleSpellCheck(self, e):
        self._view._lvOut.controls.clear()
        txtIn = self._view._txtInSentence.value
        if txtIn == "":
            self._view._lvOut.controls.append(
                ft.Text("Attention please: enter a non-empty sentence", color="red")
            )
            self._view.update()
            return

        language = self._view._drdwLanguage.value
        if language == None:
            self._view._lvOut.controls.append(
                ft.Text("Attention please: select a language", color="red")
            )
            self._view.update()
            return

        modality = self._view._drdwResearch.value
        if modality == None:
            self._view._lvOut.controls.append(
                ft.Text("Attention please: select a type of research", color="red")
            )
            self._view.update()
            return


        paroleErrate, tempo = self.handleSentence(txtIn, language, modality)

        self._view._lvOut.controls.append(
            ft.Text(f"Frase inserita: {txtIn}\n\n"
                    f"Parole Errate: {paroleErrate}\n\n"
                    f"Tempo richiesto dalla ricerca: {tempo}")
        )
        self._view._txtInSentence.value = ""
        self._view.update()




    def checkLanguage(self, e):
        language = self._view._drdwLanguage.value
        if language == "italian":
            self._view._lvOut.controls.append(
                ft.Text("Language selected: italiano")
            )
            self._view.update()
        if language == "english":
            self._view._lvOut.controls.append(
                ft.Text("Language selected: english")
            )
            self._view.update()
        if language == "spanish":
            self._view._lvOut.controls.append(
                ft.Text("Language selected: espanol")
            )
            self._view.update()

    def checkResearch(self, e):
        research = self._view._drdwResearch.value
        if research == "Default":
            self._view._lvOut.controls.append(
                ft.Text("Type of research selected: 'default'")
            )
            self._view.update()
        if research == "Linear":
            self._view._lvOut.controls.append(
                ft.Text("Type of research selected: linear")
            )
            self._view.update()
        if research == "Dichotomic":
            self._view._lvOut.controls.append(
                ft.Text("Type of research selected: dichotomic")
            )
            self._view.update()


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text