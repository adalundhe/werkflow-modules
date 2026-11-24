from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .translate_encryption_key import TranslateEncryptionKey


class TranslateTerminologyProperties(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Arn: StrictStr | None = None
    SourceLanguageCode: StrictStr | None = None
    TargetLanguageCodes: list[StrictStr] | None = None
    EncryptionKey: TranslateEncryptionKey | None = None
    SizeBytes: StrictInt | None = None
    TermCount: StrictInt | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    LastUpdatedAt: datetime.datetime | StrictStr | None = None
    Directionality: StrictStr | None = None
    Message: StrictStr | None = None
    SkippedTermCount: StrictInt | None = None
    Format: StrictStr | None = None
