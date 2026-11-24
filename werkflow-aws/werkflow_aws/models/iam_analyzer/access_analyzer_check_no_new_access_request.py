from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AccessAnalyzerCheckNoNewAccessRequest(BaseModel):
    newPolicyDocument: StrictStr
    existingPolicyDocument: StrictStr
    policyType: Literal['IDENTITY_POLICY', 'RESOURCE_POLICY']
