from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightOneDriveClientCredentials(BaseModel):
    KmsKeyArn: StrictStr
    CertThumbprint: StrictStr
