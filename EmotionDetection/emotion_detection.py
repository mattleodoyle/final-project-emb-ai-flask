import requests

def emotion_detector(text_to_analyze):
    ''' This function detects emotion in text by passing it the IBM Watson API.
        It returns a dict of emotion scores.
 
    '''
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    #send request to API save response
    response = requests.post(URL, json = input_json, headers = headers)

    #check for errors
    status = response.status_code
    if status == 400:
        emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return emotions
    
    #3convert to json
    response = response.json()

    #parse response 
    emotions = {}
    dom = 0
    for emotion, score in response['emotionPredictions'][0]['emotion'].items():
        emotions[emotion] = emotions.get(emotion, 0) + score
        if score > dom:
            emotions['dominant_emotion'] = emotion
            dom = score

    return emotions

