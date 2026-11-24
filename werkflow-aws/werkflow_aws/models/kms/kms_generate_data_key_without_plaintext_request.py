from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class KMSGenerateDataKeyWithoutPlaintextRequest(BaseModel):
    KeyId: StrictStr
    EncryptionContext: dict[StrictStr, StrictStr] | None = None
    KeySpec: Literal['AES_256', 'AES_128'] | None = None
    NumberOfBytes: StrictInt | None = None
    GrantTokens: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
