import os
from dotenv import load_dotenv
from elevenlabs import Voice, VoiceSettings, generate, play

load_dotenv()
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

def texttospeech(text, 
                 voice_id='EXAVITQu4vr4xnSDxMaL', 
                 stability=0.71, 
                 similarity_boost=0.5, 
                 style=0.0, 
                 use_speaker_boost=True): 
    
    print(ELEVEN_API_KEY)
    audio = generate(
        api_key=ELEVEN_API_KEY,
        text=text,
        voice=Voice(
            voice_id=voice_id,
            settings=VoiceSettings(
                stability=stability, 
                similarity_boost=similarity_boost, 
                style=style, 
                use_speaker_boost=use_speaker_boost
            )
        )
    )
    
    play(audio)

if __name__ == "__main__":
    text = "Born and raised in the charming south, I can add a touch of sweet southern hospitality to your audiobooks and podcasts"
    texttospeech(text)