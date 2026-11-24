from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .transcribe_vocabulary_phrase import TranscribeVocabularyPhrase


class TranscribeVocabularySettingsEntry(BaseModel):
    Language: Literal['en', 'es', 'fr', 'it', 'de', 'ja', 'pt', 'ko', 'zh-CN', 'zh-TW', 'zh-HK']
    VocabularyName: StrictStr | None = None
    Phrases: list[TranscribeVocabularyPhrase] | None = None
