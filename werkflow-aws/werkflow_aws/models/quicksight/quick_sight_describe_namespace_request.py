from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeNamespaceRequest(BaseModel):
    AwsAccountId: StrictStr
    Namespace: StrictStr
