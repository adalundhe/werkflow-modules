from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteAccessControlApplicationSecretRequest(BaseModel):
    AwsAccountId: StrictStr
    ApplicationId: StrictStr
    ClientSecretId: StrictStr
