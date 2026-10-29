import requests

def emotion_detector(text_to_analyse):
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(
        url,
        headers=headers,
        json={"raw_document": {"text": text_to_analyse}}
    )

    if response.status_code == 200:
        emotions = response.json()["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)
        return {
            **emotions,
            "dominant_emotion": dominant_emotion
        }

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    return None
