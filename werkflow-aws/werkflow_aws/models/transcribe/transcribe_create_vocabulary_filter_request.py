from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transcribe_encryption_configuration import TranscribeEncryptionConfiguration
from .transcribe_tag import TranscribeTag


class TranscribeCreateVocabularyFilterRequest(BaseModel):
    VocabularyFilterName: StrictStr
    LanguageCode: StrictStr
    Words: list[StrictStr] | None = None
    VocabularyFilterFileUri: StrictStr | None = None
    Tags: list[TranscribeTag] | None = None
    DataAccessRoleArn: StrictStr | None = None
    EncryptionConfiguration: TranscribeEncryptionConfiguration | None = None
