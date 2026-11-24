from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeDefaultQBusinessApplicationRequest(BaseModel):
    AwsAccountId: StrictStr
    Namespace: StrictStr | None = None
