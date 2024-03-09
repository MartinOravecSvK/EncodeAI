from elevenlabs import Voice, VoiceSettings, generate, play

audio = generate(
    # api_key="YOUR_API_KEY", (Defaults to os.getenv(ELEVEN_API_KEY))
    text="Hello! My name is Bella.",
    voice=Voice(
        voice_id='EXAVITQu4vr4xnSDxMaL',
        settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
    )
)

play(audio)