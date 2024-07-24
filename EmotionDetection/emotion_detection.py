import requests, json

def emotion_detection(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers = header)

    formatted_response = json.loads(response.text)

    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

    dominant_emotion = None
    max_score = 0

    for emotion, score in emotion_scores.items():
        if score > max_score:
            max_score = score
            dominant_emotion = emotion
    
    output = {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
    }

    return output