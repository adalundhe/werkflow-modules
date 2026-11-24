from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteNamespaceRequest(BaseModel):
    AwsAccountId: StrictStr
    Namespace: StrictStr
