from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class OrganizationsListInboundResponsibilityTransfersRequest(BaseModel):
    Type: Literal['BILLING']
    Id: StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
