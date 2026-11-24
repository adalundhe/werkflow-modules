from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .transcribe_encryption_configuration import TranscribeEncryptionConfiguration
from .transcribe_input_data_config import TranscribeInputDataConfig
from .transcribe_tag import TranscribeTag


class TranscribeCreateLanguageModelRequest(BaseModel):
    LanguageCode: Literal['en-US', 'hi-IN', 'es-US', 'en-GB', 'en-AU', 'de-DE', 'ja-JP']
    BaseModelName: Literal['NarrowBand', 'WideBand']
    ModelName: StrictStr
    InputDataConfig: TranscribeInputDataConfig
    EncryptionConfiguration: TranscribeEncryptionConfiguration | None = None
    Tags: list[TranscribeTag] | None = None
