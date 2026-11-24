from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .transcribe_encryption_configuration import TranscribeEncryptionConfiguration


class TranscribeGetVocabularyResponse(BaseModel):
    VocabularyName: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    VocabularyState: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    DownloadUri: StrictStr | None = None
    DataAccessRoleArn: StrictStr | None = None
    EncryptionConfiguration: TranscribeEncryptionConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
