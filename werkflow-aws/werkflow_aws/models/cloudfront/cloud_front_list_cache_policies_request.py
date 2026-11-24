from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFrontListCachePoliciesRequest(BaseModel):
    Type: Literal['managed', 'custom'] | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
