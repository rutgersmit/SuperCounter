import time
import azure.cognitiveservices.speech as speechsdk

hitword = 'super'
hits = 0

def start_counting():
    speech_config = speechsdk.SpeechConfig(
        subscription='12345', region='westeurope')
    speech_config.speech_recognition_language = 'nl-NL'
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    speech_recognizer.recognized.connect(
        lambda evt: count_word(evt.result.text))

    print('Started listening for the word \'{}\''.format(hitword))

    speech_recognizer.start_continuous_recognition()

    input("Press any key to stop...")


def count_word(input):
    global hits
    c = input.lower().count(hitword.lower())
    if c > 0:
        hits += c
        print('{} has been said {} times in this sentence, and {} in total'.format(
            hitword, c, hits))
        print('Context: {}'.format(input))


def main():
    start_counting()

    input("Press any key to stop...")
    print('We found {} times in total'.format(hits))

if __name__ == "__main__":
    main()
