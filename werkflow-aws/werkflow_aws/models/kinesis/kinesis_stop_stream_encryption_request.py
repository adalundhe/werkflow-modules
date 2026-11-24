from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class KinesisStopStreamEncryptionRequest(BaseModel):
    EncryptionType: Literal['NONE', 'KMS']
    KeyId: StrictStr
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
