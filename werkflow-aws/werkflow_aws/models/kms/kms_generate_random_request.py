from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kms_recipient_info import KMSRecipientInfo


class KMSGenerateRandomRequest(BaseModel):
    NumberOfBytes: StrictInt | None = None
    CustomKeyStoreId: StrictStr | None = None
    Recipient: KMSRecipientInfo | None = None
