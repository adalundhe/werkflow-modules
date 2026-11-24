from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AccessAnalyzerListAnalyzersRequest(BaseModel):
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    type: Literal['ACCOUNT', 'ORGANIZATION', 'ACCOUNT_UNUSED_ACCESS', 'ORGANIZATION_UNUSED_ACCESS', 'ACCOUNT_INTERNAL_ACCESS', 'ORGANIZATION_INTERNAL_ACCESS'] | None = None
