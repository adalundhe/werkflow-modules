from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .lex_audio_filler_settings import LexAudioFillerSettings
from .lex_generative_ai_settings import LexGenerativeAISettings
from .lex_speaker_diarization_settings import LexSpeakerDiarizationSettings
from .lex_speech_recognition_settings import LexSpeechRecognitionSettings
from .lex_unified_speech_settings import LexUnifiedSpeechSettings
from .lex_voice_settings import LexVoiceSettings


class LexUpdateBotLocaleRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    nluIntentConfidenceThreshold: StrictFloat | StrictInt
    description: StrictStr | None = None
    voiceSettings: LexVoiceSettings | None = None
    unifiedSpeechSettings: LexUnifiedSpeechSettings | None = None
    audioFillerSettings: LexAudioFillerSettings | None = None
    speechRecognitionSettings: LexSpeechRecognitionSettings | None = None
    generativeAISettings: LexGenerativeAISettings | None = None
    speechDetectionSensitivity: Literal['Default', 'HighNoiseTolerance', 'MaximumNoiseTolerance'] | None = None
    speakerDiarizationSettings: LexSpeakerDiarizationSettings | None = None
