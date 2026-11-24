from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUpdateAccessControlApplicationSecretRequest(BaseModel):
    AwsAccountId: StrictStr
    ApplicationId: StrictStr
    ClientSecretId: StrictStr
    UpdateRegionalSecretManagerArns: dict[StrictStr, StrictStr] | None = None
    RemoveRegionalSecretManagerArns: list[StrictStr] | None = None
