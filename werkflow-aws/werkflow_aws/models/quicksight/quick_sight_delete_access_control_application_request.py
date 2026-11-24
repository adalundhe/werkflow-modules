from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteAccessControlApplicationRequest(BaseModel):
    AwsAccountId: StrictStr
    ApplicationId: StrictStr | None = None
    IdcApplicationArn: StrictStr | None = None
