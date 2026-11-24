from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .lex_audio_filler_settings import LexAudioFillerSettings
from .lex_bot_locale_history_event import LexBotLocaleHistoryEvent
from .lex_generative_ai_settings import LexGenerativeAISettings
from .lex_speaker_diarization_settings import LexSpeakerDiarizationSettings
from .lex_speech_recognition_settings import LexSpeechRecognitionSettings
from .lex_unified_speech_settings import LexUnifiedSpeechSettings
from .lex_voice_settings import LexVoiceSettings


class LexDescribeBotLocaleResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    localeName: StrictStr | None = None
    description: StrictStr | None = None
    nluIntentConfidenceThreshold: StrictFloat | StrictInt | None = None
    voiceSettings: LexVoiceSettings | None = None
    unifiedSpeechSettings: LexUnifiedSpeechSettings | None = None
    audioFillerSettings: LexAudioFillerSettings | None = None
    speechRecognitionSettings: LexSpeechRecognitionSettings | None = None
    intentsCount: StrictInt | None = None
    slotTypesCount: StrictInt | None = None
    botLocaleStatus: StrictStr | None = None
    failureReasons: list[StrictStr] | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    lastBuildSubmittedDateTime: datetime.datetime | StrictStr | None = None
    botLocaleHistoryEvents: list[LexBotLocaleHistoryEvent] | None = None
    recommendedActions: list[StrictStr] | None = None
    generativeAISettings: LexGenerativeAISettings | None = None
    speechDetectionSensitivity: StrictStr | None = None
    speakerDiarizationSettings: LexSpeakerDiarizationSettings | None = None
    ResponseMetadata: dict[str, Any] | None = None
