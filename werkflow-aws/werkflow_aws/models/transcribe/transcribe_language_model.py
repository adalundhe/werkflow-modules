from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .transcribe_encryption_configuration import TranscribeEncryptionConfiguration
from .transcribe_input_data_config import TranscribeInputDataConfig


class TranscribeLanguageModel(BaseModel):
    ModelName: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LanguageCode: StrictStr | None = None
    BaseModelName: StrictStr | None = None
    ModelStatus: StrictStr | None = None
    UpgradeAvailability: StrictBool | None = None
    FailureReason: StrictStr | None = None
    InputDataConfig: TranscribeInputDataConfig | None = None
    EncryptionConfiguration: TranscribeEncryptionConfiguration | None = None
