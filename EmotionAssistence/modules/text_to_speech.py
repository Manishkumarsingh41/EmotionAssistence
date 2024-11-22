import azure.cognitiveservices.speech as speechsdk

def speak(text):
    """
    Converts text to speech using Azure Cognitive Services.
    """
    try:
        # Replace with your Azure Speech key and region
        speech_key = "YOUR_AZURE_SPEECH_KEY"
        service_region = "YOUR_REGION"
        
        speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        
        result = speech_synthesizer.speak_text_async(text).get()
        if result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"Error: {result.reason}")
    except Exception as e:
        print(f"Error in text-to-speech conversion: {e}")
