from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUpdateDefaultQBusinessApplicationRequest(BaseModel):
    AwsAccountId: StrictStr
    ApplicationId: StrictStr
    Namespace: StrictStr | None = None
