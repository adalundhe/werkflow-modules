from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .translate_encryption_key import TranslateEncryptionKey
from .translate_parallel_data_config import TranslateParallelDataConfig


class TranslateParallelDataProperties(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    SourceLanguageCode: StrictStr | None = None
    TargetLanguageCodes: list[StrictStr] | None = None
    ParallelDataConfig: TranslateParallelDataConfig | None = None
    Message: StrictStr | None = None
    ImportedDataSize: StrictInt | None = None
    ImportedRecordCount: StrictInt | None = None
    FailedRecordCount: StrictInt | None = None
    SkippedRecordCount: StrictInt | None = None
    EncryptionKey: TranslateEncryptionKey | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    LastUpdatedAt: datetime.datetime | StrictStr | None = None
    LatestUpdateAttemptStatus: StrictStr | None = None
    LatestUpdateAttemptAt: datetime.datetime | StrictStr | None = None
