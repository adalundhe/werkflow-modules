from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class OrganizationsListOutboundResponsibilityTransfersRequest(BaseModel):
    Type: Literal['BILLING']
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
