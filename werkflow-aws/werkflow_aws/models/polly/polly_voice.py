from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .polly_customer_managed_encryption import PollyCustomerManagedEncryption
from .polly_voice_creation_data import PollyVoiceCreationData


class PollyVoice(BaseModel):
    Arn: StrictStr | None = None
    Gender: StrictStr | None = None
    Id: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    LanguageName: StrictStr | None = None
    Name: StrictStr | None = None
    Origin: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
    AdditionalLanguageCodes: list[StrictStr] | None = None
    SupportedEngines: list[StrictStr] | None = None
    VoiceCreationData: PollyVoiceCreationData | None = None
    CustomerManagedEncryption: PollyCustomerManagedEncryption | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
