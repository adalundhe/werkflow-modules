from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .access_analyzer_access import AccessAnalyzerAccess


class AccessAnalyzerCheckAccessNotGrantedRequest(BaseModel):
    policyDocument: StrictStr
    access: list[AccessAnalyzerAccess]
    policyType: Literal['IDENTITY_POLICY', 'RESOURCE_POLICY']
