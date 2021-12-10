from nltk.stem import PorterStemmer
# import nltk
from nltk import WordNetLemmatizer
from nltk import word_tokenize , pos_tag
from nltk.corpus import stopwords
# from nltk.tokenize.sonority_sequencing import SyllableTokenizer
# from nltk.util import pr
import string

from googletrans import Translator


def translate_to_english(input_sent):
    translator = Translator()
    trans_sent = translator.translate(input_sent).text
    return trans_sent


def process_text(original_sent):

    print("\n----------- Text Processing -----------\n")
    print("\n\nOriginal Raw Sentence :  ",original_sent)



    # Any language to English Only
    english_trans_sent = translate_to_english(original_sent)
    english_trans_sent = english_trans_sent.lower()
    print("\n\nEnglish Translated Sentence :  ",english_trans_sent)    


        
    # Tokenization
    # print("\n\n------ Tokens ------ ")
    tokens = word_tokenize(english_trans_sent)
    print("\n\nTokens :  ",tokens)



    # POS TAG
    # print("\n\n------ Parts of Speech Tagging ------ ")
    tagg = pos_tag(tokens, tagset='universal')
    print("\n\nPOS TAG :  ",tagg)



    # Reordering by grammer rules
    # print("\n\n------ Reordering Sentences ------\n       by Grammer Rules")
    ps = PorterStemmer()
    lemmatizer = WordNetLemmatizer()


    # verb_tagg = []
    # reordered_tagg = []
    # for tag in tagg:
    #     if(tag[1] == "VERB"):
    #         verb_tagg.append(lemmatizer.lemmatize(tag[0], pos = 'v'), tag[1])
    #     else:
    #         reordered_tagg.append(tagg)

    # reordered_tagg.extend(verb_tagg)
    # print("\n\nReordered by Grammer Rules :  ",reordered_tagg)

    question_words_set = {"what", "which", "who", "where", "why", "when", "how", "whose"}
    negation_words = {"neither", "never", "no" "nobody", "none", "no one", "nor", "not", "nothing", "nowhere"}
    verb_string = ""
    reordered_sent = ""
    stopwords_encounterred = ""
    question_word = ""
    stop_words = set(stopwords.words('english'))
    for tag in tagg:
        if(tag[1] == "VERB" and tag[0] not in stop_words):
            verb_string +=(lemmatizer.lemmatize(tag[0], pos = 'v') + " ")
        
        elif(tag[0] in question_words_set):
            question_word += (tag[0] + " ")

        elif(tag[1] == "PRON" or tag[0] in negation_words):
            reordered_sent += (tag[0] + " ")

        elif(tag[0] not in stop_words and tag[0] not in string.punctuation and tag[0][0] not in ["'", "’"]):
            reordered_sent+=(tag[0] + " ")

        else:
            stopwords_encounterred += (tag[0] + " ")

    processed_sent = reordered_sent + question_word + verb_string
    print("\n\nStop Words Found are:  ",stopwords_encounterred)
    print("\n\nAfter Lemmatization Reordered and Removal of Stopwards :   ",processed_sent)
    print("\n\n\n---------------------------------------\n")
    return processed_sent



if __name__ == '__main__':
    # original_sent = "हम शनिवार को पार्टी करने जाने वाले हैं"
    original_sent = "मेरे बॉस के पास 3 कारें हैं"
    # original_sent = "Smit was studying in the Library"
    # original_sent = "Who are you"
    # original_sent = "He has 10 accounts"
    # original_sent = "where are you going"
    original_sent ="Is is < cold in december?"
    # original_sent = "कल मेरे बॉस ने खाने पर मुझे बुलाया था फिर मैं उनके घर गया तो मुझे खाना ही नहीं मिला और मैं घर वापस आ गया और फिर मैंने घर पर आकर गाना गाया"
    # print(set(string.punctuation))
    processed_text = process_text(original_sent)
    print("\n\n<<<<  Final Processed Text :  ", processed_text,"\n\n\n")

