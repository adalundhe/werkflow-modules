from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transcribe_encryption_configuration import TranscribeEncryptionConfiguration


class TranscribeUpdateVocabularyFilterRequest(BaseModel):
    VocabularyFilterName: StrictStr
    Words: list[StrictStr] | None = None
    VocabularyFilterFileUri: StrictStr | None = None
    DataAccessRoleArn: StrictStr | None = None
    EncryptionConfiguration: TranscribeEncryptionConfiguration | None = None
