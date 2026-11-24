from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transcribe_encryption_configuration import TranscribeEncryptionConfiguration


class TranscribeUpdateLanguageModelRequest(BaseModel):
    ModelName: StrictStr
    DataAccessRoleArn: StrictStr | None = None
    EncryptionConfiguration: TranscribeEncryptionConfiguration | None = None
