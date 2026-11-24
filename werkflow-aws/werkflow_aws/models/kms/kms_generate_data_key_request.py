from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .kms_recipient_info import KMSRecipientInfo


class KMSGenerateDataKeyRequest(BaseModel):
    KeyId: StrictStr
    EncryptionContext: dict[StrictStr, StrictStr] | None = None
    NumberOfBytes: StrictInt | None = None
    KeySpec: Literal['AES_256', 'AES_128'] | None = None
    GrantTokens: list[StrictStr] | None = None
    Recipient: KMSRecipientInfo | None = None
    DryRun: StrictBool | None = None
