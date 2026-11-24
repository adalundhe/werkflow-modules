from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .transcribe_vocabulary_filter_entry import TranscribeVocabularyFilterEntry


class TranscribeVocabularyFilterSettings(BaseModel):
    VocabularyFilterMethod: Literal['remove', 'mask', 'tag']
    Filters: list[TranscribeVocabularyFilterEntry]
