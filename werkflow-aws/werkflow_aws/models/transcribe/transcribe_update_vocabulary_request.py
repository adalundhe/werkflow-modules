from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transcribe_encryption_configuration import TranscribeEncryptionConfiguration


class TranscribeUpdateVocabularyRequest(BaseModel):
    VocabularyName: StrictStr
    LanguageCode: StrictStr
    Phrases: list[StrictStr] | None = None
    VocabularyFileUri: StrictStr | None = None
    DataAccessRoleArn: StrictStr | None = None
    EncryptionConfiguration: TranscribeEncryptionConfiguration | None = None
