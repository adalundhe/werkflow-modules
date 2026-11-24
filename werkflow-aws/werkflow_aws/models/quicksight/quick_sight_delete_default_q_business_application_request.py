from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteDefaultQBusinessApplicationRequest(BaseModel):
    AwsAccountId: StrictStr
    Namespace: StrictStr | None = None
