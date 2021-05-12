import json
import requests
from apiclient.discovery import build
from GoogleNews import GoogleNews
from PyDictionary import PyDictionary
from udpy import UrbanClient
import wikipediaapi
from wiktionaryparser import WiktionaryParser
from PyDictionary import PyDictionary
from youtubesearchpython import VideosSearch
import asyncio


def youtubeDict(word):
    output = ""

    videosSearch = VideosSearch(word)

    results = videosSearch.result()

    resultList = results['result']

    types = [sub['type'] for sub in resultList]
    ids = [sub['id'] for sub in resultList]
    titles = [sub['title'] for sub in resultList]
    publishedTimes = [sub['publishedTime'] for sub in resultList]
    durations = [sub['duration'] for sub in resultList]

    viewCounts = [sub['viewCount'] for sub in resultList]
    views = [sub['text'] for sub in viewCounts]
    viewsShortened = [sub['short'] for sub in viewCounts]

    thumbNails = [sub['thumbnails'] for sub in resultList]
    richThumbnails = [sub['richThumbnail'] for sub in resultList]
    descriptionSnippets = [sub['descriptionSnippet'] for sub in resultList]

    channels = [sub['channel'] for sub in resultList]
    channelNames = [sub['name'] for sub in channels]

    """
    These parts are not needed.
    It may cause errors if the channel did not set its profile picture.
    channelPictureInfoList = [sub['thumbnails'] for sub in channels]
    channelPictureInfo = channelPictureInfoList[0]
    channelPictureURLs = [sub['url'] for sub in channelPictureInfo]
    """

    channelLinks = [sub['link'] for sub in channels]

    accessibilities = [sub['accessibility'] for sub in resultList]
    links = [sub['link'] for sub in resultList]
    shelfTitles = [sub['shelfTitle'] for sub in resultList]

    for i in range(0, 3):
        output += "ID: " + ids[i] + "\n"
        output +="Title: " + titles[i] + "\n"
        output +="Link: " + links[i] + "\n"
    

    return output

def wordnetDict(word):
    dictionary = PyDictionary()
    
    output = ""

    results = dictionary.meaning(word)
    partOfSpeechList = []
    definitionList = []

    if results == None:
        output += "The " +  word + " is not found on WordNet."
    else:
        for result in results:
            partOfSpeechList.append(result)
            definitionList.append(results.get(result)[0])

        for i in range(len(definitionList)):
            output += "Result"+ str(i+1) + ":" +"\n"
            output += "Part of speech: "+ partOfSpeechList[i] +"\n"
            output += "Definition: "+ definitionList[i]+"\n"
    
    return output[:-1]

def wiktionaryDict(word):
    output = ""
    
    jsonParser = WiktionaryParser()
    jsonResult = jsonParser.fetch(word)

    if jsonResult == []:
        output = word + " is not found on Wiktionary"
    else:
        dictResult = jsonResult[0]

        pronunciations = dictResult.get("pronunciations")
        pronunciationText = pronunciations.get("text")
        pronunciationAudio = pronunciations.get("audio")

        definitionList = dictResult.get("definitions")
        definitions = definitionList[0]

        relatedWordList = definitions.get("relatedWords")
        relatedWords = relatedWordList[0]

        textList = definitions.get("text")
        texts = textList[0]

        partOfSpeech = definitions.get("partOfSpeech")
        examples = definitions.get("examples")

        etymology = dictResult.get("etymology")

        output += "Definitions:" +"\n"
        output += texts + "\n"
        output += "\n"
        
        output +="Part of speech: " + partOfSpeech +"\n"
        output += "\n"

        output += "Example: " +"\n"
        for j in range(0, 3):
            output += str(j+1) + ". " + examples[j] +"\n"

    return output

def mwcDict(word):
    output = ""

    apiKey  = "c33d59f0-4576-4dfc-a389-918e5316421b"
    
    wordURL = "https://dictionaryapi.com/api/v3/references/collegiate/json/"+ word + "?key=" + apiKey

    result = requests.get(wordURL)

    jsonResult = json.dumps(result.json())

    dictionaryResult = json.loads(jsonResult)

    stems = [] #lists all of the entry's headwords, variants, inflections, undefined entry words, and defined run-on phrases. Each stem string is a valid search term that should match this entry.
    partOfSpeeches = []
    definitionResults = []
    shortDefinitionResults = []

    for i in range(3):
        output += "Counter: "
        
        stemList = dictionaryResult[i].get('meta').get('stems')
        
        output += stemList[0] + "</br>"
        
        partOfSpeech = dictionaryResult[i].get('fl')
        output +="Part of speech: " + partOfSpeech  + "</br>"
        partOfSpeeches.append(partOfSpeech)
        
        shortdefList = dictionaryResult[i].get('shortdef')
        output +="Short definitons: " + "</br>"
        for j in range(0, len(shortdefList)):
            output += str(j+1) + ". " + shortdefList[j] + "</br>"
            shortDefinitionResults.append(shortdefList[j])

    return output

def mwlDict(word):
    output = ""

    apiKey  = "c0fe6dc9-3217-4825-b6ad-fac424c7d7b3"

    wordURL = "https://dictionaryapi.com/api/v3/references/learners/json/"+ word + "?key=" + apiKey
    result = requests.get(wordURL)

    jsonResult = json.dumps(result.json())

    dictionaryResult = json.loads(jsonResult)

    stems = [] #lists all of the entry's headwords, variants, inflections, undefined entry words, and defined run-on phrases. Each stem string is a valid search term that should match this entry.
    partOfSpeeches = []
    definitionResults = []
    shortDefinitionResults = []

    for i in range(3):
        output += "Counter: "
        
        stemList = dictionaryResult[i].get('meta').get('stems')
        
        output += stemList[0] + "</br>"
        
        partOfSpeech = dictionaryResult[i].get('fl')
        output +="Part of speech: " + partOfSpeech  + "</br>"
        partOfSpeeches.append(partOfSpeech)
        
        shortdefList = dictionaryResult[i].get('shortdef')
        output +="Short definitons: " + "</br>"
        for j in range(0, len(shortdefList)):
            output += str(j+1) + ". " + shortdefList[j] + "</br>"
            shortDefinitionResults.append(shortdefList[j])

    return output

def googleImageDict(word):
    output = ""
    apiKey = "AIzaSyCB-M_Z2BlLfWgAMOuhLmNHHmoBoRCme50"
    searchEngineID = "4c4e5dd8e9cf81ff8"

    resource = build("customsearch", "v1", developerKey=apiKey).cse()
    results = resource.list(q=word, cx=searchEngineID, searchType='image').execute()

    resultURL = results.get('url').get('template')
    imageDataSet = results.get('items')

    for i in range(0, 3):
        image = imageDataSet[i].get('image')

        link = imageDataSet[i].get('link')
        contextLink = image.get('contextLink')

        output += "<a href=\'" + link + "\' height=\'5\' width=\'10\'><img src=\' "+ contextLink +" \' alt=\'context link.\'><a>\n"

    return output

def etymonlineDict(word):
    baseURL = "https://www.etymonline.com/"
    queryURL = "search?q=" + word.replace(" ", "+")
    wordURL = baseURL + queryURL

    return wordURL

def googleNewsDict(word):
    output = ''

    googlenews = GoogleNews(lang='en')
    
    googlenews.search(word)

    result = googlenews.result()
    for i in range(5):
        res = result[i]
        link = res['link']
        title = res['title']
        output += '<a href=\'' + link + '\'>' + title + '</a>\n'

    return output[:-1]

def oxfordDict(word):
    output = ""
    appID  = "501e439d"
    appKey  = "f7bd8a4c25db428d6b1f972d3acc85d7"
    endPoint = "entries"
    languageCode = "en-us"

    wordURL = "https://od-api.oxforddictionaries.com/api/v2/" + endPoint + "/" + languageCode + "/" + word.lower()

    result = requests.get(wordURL, headers = {"app_ID": appID, "app_Key": appKey})


    jsonResult = json.dumps(result.json())

    dictionaryResult = json.loads(jsonResult)

    realResultList = dictionaryResult["results"]
    realResultDict = realResultList[0]

    resultInfoList = realResultDict["lexicalEntries"]
    resultInfoDict = resultInfoList[0]
    resultDataList = resultInfoDict["entries"]
    resultDataDict = resultDataList[0]


    wordSensesList = resultDataDict["senses"]

    wordResult = {}
    for dict in wordSensesList:
        for list in dict:
            if list in wordResult:
                wordResult[list] += (dict[list])
            else:
                wordResult[list] = dict[list]

    output += "Definitions:"+ "\n"
    definitionList = wordResult.get("definitions")
    for i in range(0, len(definitionList)):
        output += str(i+1) + ". " + definitionList[i] + "\n"
    output += "\n"

    output += "Examples: "+ "\n"
    exampleList = wordResult.get("examples")
    if exampleList == None:
        output += "No example" + "\n"
    else:
        for i in range(0, len(exampleList)):
            output += str(i+1) + ". " + exampleList[i].get("text") +"\n"

    return output[:-1]

def synonymDict(word):
    syn_output = ""
    ant_output = ""
    
    thesaurus = PyDictionary()

    synonyms = thesaurus.synonym(word)
    if synonyms == None:
        syn_output = "There is no synonym founded at synonym.com"
    else:
        syn_output += "Here are the synonyms for the following word: " + word + "\n"
        for i in range(0, len(synonyms)):
            syn_output += str(i+1) + ". " + synonyms[i] + "\n"

    antonyms = thesaurus.antonym(word)
    if antonyms == None:
        ant_output = "There is no antonym founded at synonym.com"
    else:
        ant_output += "Here are the antonyms for the following word:" + word + "\n"
        for j in range(0, len(antonyms)):
            ant_output += str(j+1) + ". " + antonyms[j] + '\n'

    output = syn_output + "\n" + ant_output

    return output

def thefreedictionaryDict(word):
    baseURL = "http://www.thefreedictionary.com/"
    queryURL = word.replace(" ", "+")
    wordURL = baseURL + queryURL

    return wordURL

def urbanDict(word):
    output = ""
    client = UrbanClient()
    definitions = client.get_definition(word)

    i = 0
    while i < 3:
        for lexis in definitions:
            i = i + 1
            output += "Definition " + str(i) + ":\n"
            output += lexis.definition + "\n"
            
            output += "Example " + str(i) + ": \n"
            output += lexis.example + "\n"
        output += "\n" 

    output += "Link for the results searched: https://www.urbandictionary.com/define.php?term="+word

    return output

def wikiDict(word):
    output = ""

    wikiResult = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)
    wikiPage = wikiResult.page(word)

    output += "Page - Summary: " + wikiPage.summary +"\n"
    output += "\n"
    output += "Full URL: " + wikiPage.fullurl +"\n"

    return output