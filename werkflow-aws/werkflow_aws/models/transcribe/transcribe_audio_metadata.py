from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .transcribe_sync_language_code_item import TranscribeSyncLanguageCodeItem


class TranscribeAudioMetadata(BaseModel):
    LanguageCode: StrictStr | None = None
    LanguageCodes: list[TranscribeSyncLanguageCodeItem] | None = None
    MediaFormat: StrictStr | None = None
    MediaSampleRateHertz: StrictInt | None = None
    SpeakersCount: StrictInt | None = None
    NumberOfChannels: StrictInt | None = None
