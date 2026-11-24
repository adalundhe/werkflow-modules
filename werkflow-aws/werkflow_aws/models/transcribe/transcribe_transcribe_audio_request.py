from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt
from .transcribe_content_redaction import TranscribeContentRedaction
from .transcribe_sync_media import TranscribeSyncMedia
from .transcribe_sync_output_configuration import TranscribeSyncOutputConfiguration
from .transcribe_vocabulary_filter_settings import TranscribeVocabularyFilterSettings
from .transcribe_vocabulary_settings_entry import TranscribeVocabularySettingsEntry


class TranscribeTranscribeAudioRequest(BaseModel):
    Media: TranscribeSyncMedia
    Language: Literal['en', 'es', 'fr', 'it', 'de', 'ja', 'pt', 'ko', 'zh-CN', 'zh-TW', 'zh-HK'] | None = None
    LanguageDetectionMode: Literal['IDENTIFY_LANGUAGE'] | None = None
    LanguageOptions: list[Literal['en', 'es', 'fr', 'it', 'de', 'ja', 'pt', 'ko', 'zh-CN', 'zh-TW', 'zh-HK']] | None = None
    ChannelIdentification: StrictBool | None = None
    ShowSpeakerLabels: StrictBool | None = None
    MaxSpeakerLabels: StrictInt | None = None
    VocabularySettings: list[TranscribeVocabularySettingsEntry] | None = None
    VocabularyFilterSettings: TranscribeVocabularyFilterSettings | None = None
    ContentRedaction: TranscribeContentRedaction | None = None
    OutputConfiguration: TranscribeSyncOutputConfiguration | None = None
