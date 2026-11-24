from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSharePointClientCredentials(BaseModel):
    KmsKeyArn: StrictStr
    CertThumbprint: StrictStr
