from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .transcribe_encryption_configuration import TranscribeEncryptionConfiguration


class TranscribeGetVocabularyFilterResponse(BaseModel):
    VocabularyFilterName: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    DownloadUri: StrictStr | None = None
    DataAccessRoleArn: StrictStr | None = None
    EncryptionConfiguration: TranscribeEncryptionConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
